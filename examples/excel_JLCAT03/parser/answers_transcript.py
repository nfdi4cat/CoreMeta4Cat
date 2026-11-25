#!/usr/bin/env python3
"""Make ../source/provider_answers.md, a verbatim transcript of the data provider's answers.

The provider wrote the answers into a copy of our questions (the "Please answer" part of
../FEEDBACK_FOR_DATA_PROVIDER.md as sent in round 1) and returned it as a .docx. In that file:
- the questions are list items;
- our headings are paragraphs that equal a paragraph of the questions file;
- every other non-empty paragraph is an answer, quoted unchanged.

The questions are numbered in order (Q1-Q17), so that the provenance of the record can cite them.
Compare against the questions file as it was sent, because later rounds add text to it:

    git show ef13716e8:examples/excel_JLCAT03/FEEDBACK_FOR_DATA_PROVIDER.md > questions_round1.md
    uv run python examples/excel_JLCAT03/parser/answers_transcript.py \
        examples/excel_JLCAT03/source/provider_answers_2026-11-24.docx questions_round1.md \
        examples/excel_JLCAT03/source/provider_answers.md

The .docx is read directly from its ZIP container; nothing in it is executed.
"""
import re
import sys
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


def norm(s):
    s = re.sub(r"[*`#]", "", s)
    s = re.sub(r"^\s*(\d+\.|-)\s+", "", s)          # list marker of a markdown item
    return " ".join(s.replace("“", '"').replace("”", '"').split()).strip().casefold()


def blocks(md):
    """Paragraphs, headings and list items of the questions file, each as one normalised string."""
    out, cur = [], []
    for line in md.splitlines():
        starts_item = re.match(r"^\s*(\d+\.|-)\s+", line) or line.startswith("#")
        if not line.strip() or starts_item:
            if cur:
                out.append(norm(" ".join(cur)))
            cur = [line] if line.strip() else []
            if line.startswith("#"):
                out.append(norm(line))
                cur = []
        else:
            cur.append(line)
    if cur:
        out.append(norm(" ".join(cur)))
    return set(out)


def main():
    docx, questions, out = sys.argv[1:4]
    ours = blocks(Path(questions).read_text(encoding="utf8"))
    body = ET.fromstring(zipfile.ZipFile(docx).read("word/document.xml")).find(W + "body")
    items = []
    for p in body.findall(W + "p"):
        text = "".join(t.text or "" for t in p.iter(W + "t"))
        if not text.strip():
            continue
        if p.find(f"{W}pPr/{W}numPr") is not None:
            items.append(("q", text.strip()))
        elif norm(text) in ours:
            items.append(("h", text.strip()))
        else:
            items.append(("a", text.rstrip()))

    lines = [
        "# Answers from the data provider (2026-11-24)",
        "",
        f"Verbatim transcript of `{Path(docx).name}`. The data provider wrote the answers into a copy of the",
        "questions in `../FEEDBACK_FOR_DATA_PROVIDER.md`: questions and headings are ours as copied there,",
        "answers (quoted) are theirs, unchanged. Generated from the .docx, not retyped. The record's",
        "provenance cites the answers by question number (Q1-Q17).",
        "",
    ]
    q = 0
    for i, (kind, text) in enumerate(items):
        if kind == "h":
            lines += [f"## {text}", ""]
        elif kind == "q":
            q += 1
            lines += [f"**Q{q}.** {text}", ""]
            if i + 1 >= len(items) or items[i + 1][0] != "a":
                lines += ["> *(no answer)*", ""]
        else:
            lines += [f"> {text}", ""]
    Path(out).write_text("\n".join(lines).rstrip() + "\n", encoding="utf8", newline="\n")
    print(f"{q} questions, {sum(1 for k, _ in items if k == 'a')} answer paragraphs -> {out}")


if __name__ == "__main__":
    main()
