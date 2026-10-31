#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Check ISO's records of ISO/IEC 27001:2022 against ISO Open Data.

ISO sells the text of ISO/IEC 27001, so this repository pins what ISO
publishes openly about it instead: its records in ISO Open Data's
``iso_deliverables_metadata`` dataset, which ISO updates daily under the ODC
Attribution License (ODC-By) v1.0. Four records matter here:

- ISO/IEC 27001:2022, the edition the schema models;
- ISO/IEC 27001:2022/Amd 1:2024, its one amendment so far;
- ISO/IEC 27002:2022, the guidance for the Annex A controls, which ISO
  already lists as replaced by project 94703;
- ISO/IEC 27000:2026, the overview the standard refers to for its terms.

``src/iso27001/schema/iso-open-data/iso_deliverables_metadata.jsonl`` holds
those records as ISO published them on the pinned date, each without its
``scope`` field: a scope is a summary of the standard in ISO's words, which
this repository does not reproduce. Each record is pinned below by the
SHA-256 hash of its line.

Several things can change without any change in this repository:

- ISO publishes another amendment or a corrigendum of the pinned edition;
- ISO publishes a new edition, which replaces the pinned one;
- a pinned record changes, for example its stage when ISO confirms,
  revises or withdraws the standard;
- ISO's successor to ISO/IEC 27002:2022, project 94703, enters the dataset;
- a pinned record leaves the dataset, or ISO changes the dataset's licence;
- the extract drifts from what was pinned.

The dataset is about 80 MB. The script streams it line by line and parses
only the lines that name a pinned record or the pinned edition, so it never
holds the file in memory. It reads the dataset's licence from ISO's open data
page, through the Internet Archive's latest capture when iso.org refuses a
script, as it usually does. It sends no token anywhere. It prints a Markdown
report and exits 1 when any of the above is found or a check could not
finish.

Usage::

    python scripts/check_upstream_release.py [--report FILE]
"""

from __future__ import annotations

import argparse
import gzip
import hashlib
import html
import http.client
import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXTRACT = (
    ROOT
    / "src"
    / "iso27001"
    / "schema"
    / "iso-open-data"
    / "iso_deliverables_metadata.jsonl"
)
USER_AGENT = "lmodel-iso27001-upstream-check"

DATASET = (
    "https://isopublicstorageprod.blob.core.windows.net/opendata/_latest/"
    "iso_deliverables_metadata/json/iso_deliverables_metadata.jsonl"
)
LICENCE_PAGE = "https://www.iso.org/open-data.html"
# The Internet Archive's latest capture of the page, as it was served.
LICENCE_MIRROR = f"https://web.archive.org/web/3000id_/{LICENCE_PAGE}"

# The date the extract was taken from the dataset (its Last-Modified date).
PINNED_DATE = "2026-10-28"

# The edition the schema models. The schema header's `version` and `source`
# carry the same values, and tests/test_upstream.py holds them equal.
PINNED_EDITION = "ISO/IEC 27001:2022"
PINNED_VERSION = "2022/Amd 1:2024"
PINNED_SOURCE = "https://www.iso.org/standard/82875.html"
EDITION_ID = 82875

# Each extract line, by ISO's record id, and the SHA-256 hash of the line.
PINNED_RECORDS = {
    75652: "8541b6e65548b0c40a88835761dd6f49c57ec2329a91b711da0d38ffcb3a0840",
    82875: "558b6c3a49881116eee24e51294ff140be10c0d2e2edae797c6e1e84f3b7a647",
    84257: "ea171f34347f36bd2f49cae86afed886028843d5501966fb5dd2ac32b495b573",
    88435: "1781a7ce359b4935240575db489fe5c191bb43b26c7f7db5117a056b586c0493",
}

# ISO/IEC 27002:2022 names its successor, project 94703, in `replacedBy`,
# but the dataset holds no record of that project yet.
SUCCESSOR_PROJECTS = {94703}

# A record whose reference starts so is a supplement of the pinned edition.
SUPPLEMENT_PREFIX = f"{PINNED_EDITION}/"

# The field of a record that the extract leaves out, as the docstring says.
LEFT_OUT = ("scope",)

# What ISO's open data page names as the dataset's licence.
PINNED_LICENCE = "ODC Attribution License (ODC-By) v1.0"
PINNED_LICENCE_URL = "https://opendatacommons.org/licenses/by/1-0/"

# The stage code of a published standard. Any other is reported.
PUBLISHED = 6060


def _open(url: str):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    return urllib.request.urlopen(req, timeout=120)


def _get(url: str) -> tuple[str, bytes]:
    """The address a request ended at and the body, gunzipped if need be."""
    with _open(url) as resp:
        body = resp.read()
        final = resp.geturl()
    if body[:2] == b"\x1f\x8b":
        body = gzip.decompress(body)
    return final, body


def _lines(url: str):
    """The dataset's lines, read one at a time from the response."""
    with _open(url) as resp:
        for raw in resp:
            yield raw.decode("utf-8")


def _code(text: object) -> str:
    """Text a site chose, such as an address it redirected to, as a code
    span, so it cannot mention a person or add a link in the issue."""
    return "`" + str(text).replace("`", "'") + "`"


def line_of(record: dict) -> str:
    """A record as the extract writes it: the dataset's compact JSON, without
    the fields the extract leaves out."""
    kept = {k: v for k, v in record.items() if k not in LEFT_OUT}
    return json.dumps(kept, ensure_ascii=False, separators=(",", ":"))


def digest(line: str) -> str:
    return hashlib.sha256(line.encode("utf-8")).hexdigest()


def _extract() -> dict[int, dict]:
    """The extract's records, by id."""
    records = {}
    for line in EXTRACT.read_text(encoding="utf-8").splitlines():
        record = json.loads(line)
        records[record["id"]] = record
    return records


def _relevant(line: str) -> bool:
    """Whether a raw line may hold a record the checks need, decided without
    parsing it: a pinned or successor id anywhere in it, or the edition's
    reference. A line that matches by chance costs one parse and no more."""
    if SUPPLEMENT_PREFIX in line:
        return True
    return any(str(i) in line for i in (*PINNED_RECORDS, *SUCCESSOR_PROJECTS))


def check_extract() -> tuple[list[str], bool]:
    """Report whether the extract is the lines pinned, offline."""
    report = [
        f"- Pinned edition: {PINNED_EDITION} with its supplements, {PINNED_SOURCE}; "
        f"ISO Open Data as of {PINNED_DATE}."
    ]
    problems = []
    if not EXTRACT.is_file():
        problems.append("the extract is missing")
    else:
        lines = EXTRACT.read_text(encoding="utf-8").splitlines()
        seen = {}
        for line in lines:
            seen[json.loads(line)["id"]] = digest(line)
        for rid, pinned in sorted(PINNED_RECORDS.items()):
            if rid not in seen:
                problems.append(f"record {rid} is missing from the extract")
            elif seen[rid] != pinned:
                problems.append(f"record {rid} differs from the pinned line")
        problems += [
            f"record {rid} is in the extract but not pinned"
            for rid in sorted(seen.keys() - PINNED_RECORDS.keys())
        ]
    if problems:
        report.append(f"- **{len(problems)} problem(s) with the extract:**")
        report += [f"  - {p}" for p in problems]
        return report, True
    report.append(
        f"- The extract holds the {len(PINNED_RECORDS)} pinned records, each line as pinned."
    )
    return report, False


def check_records() -> tuple[list[str], bool]:
    """Stream the live dataset and report what changed since the pin."""
    pinned = _extract()
    live: dict[int, dict] = {}
    supplements: dict[int, dict] = {}
    successors: dict[int, dict] = {}
    for line in _lines(DATASET):
        if not _relevant(line):
            continue
        record = json.loads(line)
        rid = record["id"]
        if rid in PINNED_RECORDS:
            live[rid] = record
        if record.get("reference", "").startswith(SUPPLEMENT_PREFIX):
            supplements[rid] = record
        if rid in SUCCESSOR_PROJECTS or set(record.get("replaces") or []) & set(
            PINNED_RECORDS
        ):
            successors[rid] = record

    report, attention = [], False
    unchanged = 0
    for rid in sorted(PINNED_RECORDS):
        old = pinned.get(rid, {})
        name = old.get("reference", str(rid))
        if rid not in live:
            attention = True
            report.append(
                f"- **{name} (record {rid}) is no longer in the dataset.** Find out "
                "whether ISO withdrew it or renumbered it."
            )
            continue
        new = live[rid]
        if digest(line_of(new)) == PINNED_RECORDS[rid]:
            unchanged += 1
            continue
        attention = True
        changed = sorted(
            k
            for k in (new.keys() | old.keys()) - set(LEFT_OUT)
            if new.get(k) != old.get(k)
        )
        details = "; ".join(
            f"`{k}` from {json.dumps(old.get(k), ensure_ascii=False)} to "
            f"{json.dumps(new.get(k), ensure_ascii=False)}"
            for k in changed
        )
        report.append(f"- **{name} (record {rid}) changed:** {details}.")
        if new.get("currentStage") != PUBLISHED:
            report.append(
                f"  - Its stage is now {new.get('currentStage')}, not {PUBLISHED} "
                "(published); read ISO's stage codes to see what that means."
            )
        if new.get("replacedBy"):
            report.append(
                f"  - ISO now lists it as replaced by {new['replacedBy']}. Decide "
                "whether the schema moves to the successor."
            )
    report.append(
        f"- {unchanged} of {len(PINNED_RECORDS)} pinned records are unchanged."
    )
    for rid, record in sorted(supplements.items()):
        if rid not in PINNED_RECORDS:
            attention = True
            report.append(
                f"- **ISO lists a supplement of {PINNED_EDITION} that is not pinned: "
                f"{record.get('reference')} (record {rid}, stage "
                f"{record.get('currentStage')}).** Read it, decide what the schema "
                "changes, and add it to the extract and the header's version."
            )
    for rid, record in sorted(successors.items()):
        attention = True
        replaced = sorted(set(record.get("replaces") or []) & set(PINNED_RECORDS))
        what = (
            f"replaces record {', '.join(map(str, replaced))}"
            if replaced
            else "is the successor ISO/IEC 27002:2022 names"
        )
        report.append(
            f"- **{record.get('reference')} (record {rid}, stage "
            f"{record.get('currentStage')}) {what}.** Decide whether the schema "
            "follows it."
        )
    return report, attention


def check_licence() -> tuple[list[str], bool]:
    """Report the dataset's licence as ISO's open data page names it."""
    try:
        where, body = _get(LICENCE_PAGE)
    except urllib.error.HTTPError as err:
        if err.code not in (401, 403, 429):
            raise
        where, body = _get(LICENCE_MIRROR)
    page = body.decode("utf-8", errors="replace")
    section = page.partition('id="iso_deliverables_metadata"')[2]
    row = re.search(
        r"<td>\s*License\s*</td>\s*<td>(.*?)</td>", section, flags=re.S | re.I
    )
    if not row:
        return [
            f"- **ISO's open data page ({_code(where)}) no longer names the licence of "
            "iso_deliverables_metadata where the check looks.** Read the page."
        ], True
    href = re.search(r'href="([^"]+)"', row.group(1))
    name = html.unescape(re.sub(r"<[^>]+>", "", row.group(1))).strip()
    url = href.group(1) if href else ""
    if name != PINNED_LICENCE or url.rstrip("/") != PINNED_LICENCE_URL.rstrip("/"):
        return [
            f"- **ISO's open data page ({_code(where)}) names the dataset's licence as "
            f"{name} ({url or 'no link'}), not {PINNED_LICENCE}.** Check that the "
            "extract and NOTICE still meet its terms."
        ], True
    return [f"- Licence: {PINNED_LICENCE}, as read at {_code(where)}."], False


# Each check, by the name the report gives it when it cannot finish.
CHECKS = (
    ("extract", check_extract),
    ("records", check_records),
    ("licence", check_licence),
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--report", type=Path, help="Also write the Markdown report to this file"
    )
    args = parser.parse_args(argv)
    lines, attention = [], False
    for label, check in CHECKS:
        try:
            found, needs = check()
        # OSError covers a refused or failed fetch and a timeout,
        # HTTPException a connection cut off mid-dataset, EOFError a gzipped
        # page cut short, and ValueError a line that is not JSON or UTF-8.
        except (OSError, http.client.HTTPException, EOFError, ValueError) as err:
            found = [f"- **The {label} check could not finish: {_code(err)}.**"]
            needs = True
        lines += found
        attention = attention or needs
    text = "\n".join(lines) + "\n"
    print(text, end="")
    if args.report:
        args.report.write_text(text, encoding="utf-8")
    return 1 if attention else 0


if __name__ == "__main__":
    sys.exit(main())
