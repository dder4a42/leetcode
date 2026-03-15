#!/usr/bin/env python3
"""
Generate repository-level index.md for LeetCode workspace.

Features:
1) Defines and reads a machine-friendly subdirectory index.md format (Markdown table)
2) Auto-scans all problem folders (folder containing solution.py)
3) Outputs a root index.md with:
   - format convention
    - per-topic problem links (LeetCode / local explanation / analysis section / code)
   - a Markdown file-tree view

Subdirectory index.md format (recommended):

    # <topic name>
    > INDEX_FORMAT_V1
    |
    | slug | title | leetcode | solution | code | analysis_anchor |
    | --- | --- | --- | --- | --- | --- |
    | two_sum | Two Sum | https://leetcode.com/problems/two-sum/ | ./two_sum/README.md | ./two_sum/solution.py | two_sum |

Notes:
- Table supports 5 columns (legacy) or 6 columns (with analysis anchor).
- Relative paths are relative to this subdirectory.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Tuple


ROOT = Path(__file__).resolve().parent
OUTPUT_FILE = ROOT / "index.md"

# Skip noise folders anywhere in tree
SKIP_DIRS = {
    ".git",
    ".vscode",
    "__pycache__",
    ".ruff_cache",
    ".sii",
    ".sisyphus",
}

# Top-level folders to skip from algorithm scan
SKIP_TOP_LEVEL = {"utils", "utils_cpp"}

NOTE_CANDIDATES = ("README.md", "solution.md", "note.md", "notes.md")


@dataclass
class ProblemRecord:
    slug: str
    topic_dir: Path
    problem_dir: Path
    title: str
    leetcode_url: Optional[str]
    note_rel: Optional[Path]
    analysis_anchor: Optional[str]
    code_rel: Path

    @property
    def topic_rel(self) -> Path:
        return self.topic_dir.relative_to(ROOT)

    @property
    def problem_rel(self) -> Path:
        return self.problem_dir.relative_to(ROOT)


def is_skipped_dir(path: Path) -> bool:
    return any(part in SKIP_DIRS for part in path.parts)


def safe_rel(path: Path) -> str:
    return path.as_posix()


def md_link(text: str, target: str) -> str:
    return f"[{text}]({target})"


def find_problem_dirs() -> List[Path]:
    problems: List[Path] = []
    for p in ROOT.rglob("solution.py"):
        if is_skipped_dir(p):
            continue
        rel = p.relative_to(ROOT)
        if rel.parts and rel.parts[0] in SKIP_TOP_LEVEL:
            continue
        problems.append(p.parent)
    return sorted(set(problems), key=lambda x: x.as_posix())


def read_sub_index_table(topic_dir: Path) -> Dict[str, Dict[str, str]]:
    """Parse topic_dir/index.md table.

    Supported columns:
    - 5 columns: slug|title|leetcode|solution|code
    - 6 columns: slug|title|leetcode|solution|code|analysis_anchor
    """
    idx_file = topic_dir / "index.md"
    if not idx_file.exists():
        return {}

    text = idx_file.read_text(encoding="utf-8")
    rows: Dict[str, Dict[str, str]] = {}

    for line in text.splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        cols = [c.strip() for c in line.strip("|").split("|")]
        if len(cols) not in {5, 6}:
            continue
        if cols[0].lower() in {"slug", "---", ""}:
            continue

        if len(cols) == 5:
            slug, title, leetcode, solution, code = cols
            analysis_anchor = ""
        else:
            slug, title, leetcode, solution, code, analysis_anchor = cols
        rows[slug] = {
            "title": title,
            "leetcode": leetcode,
            "solution": solution,
            "code": code,
            "analysis_anchor": analysis_anchor,
        }
    return rows


def parse_headings(topic_dir: Path) -> Dict[str, str]:
    """Return heading text -> anchor for topic index.md.

    This uses a simplified anchor rule for slug-like headings (ASCII letters/digits/_/-),
    which is enough for entries like `### two_sum`.
    """
    idx_file = topic_dir / "index.md"
    if not idx_file.exists():
        return {}

    text = idx_file.read_text(encoding="utf-8")
    m: Dict[str, str] = {}
    for line in text.splitlines():
        line = line.strip()
        h = re.match(r"^#{1,6}\s+(.+?)\s*$", line)
        if not h:
            continue
        heading = h.group(1).strip()
        key = heading.lower()
        anchor = heading.lower().strip().replace(" ", "-")
        m[key] = anchor
    return m


def normalize_optional_value(v: str) -> Optional[str]:
    v = (v or "").strip()
    if not v or v in {"-", "N/A", "n/a", "TODO", "todo"}:
        return None
    return v


def normalize_optional_url(v: str) -> Optional[str]:
    v = v.strip()
    if not v or v in {"-", "N/A", "n/a", "TODO", "todo"}:
        return None
    if re.match(r"https?://", v):
        return v
    return None


def resolve_note(problem_dir: Path, mapped_solution: Optional[str], topic_dir: Path) -> Optional[Path]:
    if mapped_solution and mapped_solution.strip() and mapped_solution.strip() != "-":
        p = (topic_dir / mapped_solution).resolve()
        if p.exists() and p.is_file():
            return p.relative_to(ROOT)

    for name in NOTE_CANDIDATES:
        p = problem_dir / name
        if p.exists() and p.is_file():
            return p.relative_to(ROOT)
    return None


def build_records() -> List[ProblemRecord]:
    problem_dirs = find_problem_dirs()
    by_topic: Dict[Path, List[Path]] = {}
    for pdir in problem_dirs:
        topic_dir = pdir.parent
        by_topic.setdefault(topic_dir, []).append(pdir)

    records: List[ProblemRecord] = []
    for topic_dir, pdirs in sorted(by_topic.items(), key=lambda x: x[0].as_posix()):
        table_data = read_sub_index_table(topic_dir)
        heading_map = parse_headings(topic_dir)

        for pdir in sorted(pdirs, key=lambda x: x.as_posix()):
            slug = pdir.name
            mapped = table_data.get(slug, {})
            title = mapped.get("title") or slug
            leetcode = normalize_optional_url(mapped.get("leetcode", ""))
            note_rel = resolve_note(pdir, mapped.get("solution"), topic_dir)
            analysis_anchor = normalize_optional_value(mapped.get("analysis_anchor", ""))
            if not analysis_anchor and slug.lower() in heading_map:
                analysis_anchor = heading_map[slug.lower()]
            code_rel = (pdir / "solution.py").relative_to(ROOT)

            records.append(
                ProblemRecord(
                    slug=slug,
                    topic_dir=topic_dir,
                    problem_dir=pdir,
                    title=title,
                    leetcode_url=leetcode,
                    note_rel=note_rel,
                    analysis_anchor=analysis_anchor,
                    code_rel=code_rel,
                )
            )
    return records


def render_tree(records: List[ProblemRecord]) -> List[str]:
    """Markdown tree rooted at repo root; includes only algorithm folders/files."""
    tree: Dict[str, Dict[str, List[ProblemRecord]]] = {}
    for r in records:
        top = r.problem_rel.parts[0]
        topic = safe_rel(r.topic_rel)
        tree.setdefault(top, {}).setdefault(topic, []).append(r)

    lines = ["```text", "leetcode/"]
    tops = sorted(tree.keys())
    for i, top in enumerate(tops):
        top_last = i == len(tops) - 1
        top_prefix = "└── " if top_last else "├── "
        lines.append(f"{top_prefix}{top}/")
        topics = sorted(tree[top].keys())
        for j, topic in enumerate(topics):
            topic_last = j == len(topics) - 1
            indent = "    " if top_last else "│   "
            problems = sorted(tree[top][topic], key=lambda x: x.slug)

            # If topic is exactly top-level dir (e.g. double_ptr), don't render duplicated folder.
            if topic == top:
                for k, rec in enumerate(problems):
                    p_last = k == len(problems) - 1
                    p_prefix = "└── " if p_last else "├── "
                    lines.append(f"{indent}{p_prefix}{rec.slug}/")

                    leaf_indent = indent + ("    " if p_last else "│   ")
                    lines.append(f"{leaf_indent}├── solution.py")
                    if rec.note_rel and rec.note_rel.parent == rec.problem_rel:
                        lines.append(f"{leaf_indent}└── {rec.note_rel.name}")
                    else:
                        lines.append(f"{leaf_indent}└── test_cases.txt")
                continue

            topic_prefix = "└── " if topic_last else "├── "
            topic_name = topic.split("/", 1)[1] if "/" in topic else topic
            lines.append(f"{indent}{topic_prefix}{topic_name}/")

            for k, rec in enumerate(problems):
                p_last = k == len(problems) - 1
                indent2 = indent + ("    " if topic_last else "│   ")
                p_prefix = "└── " if p_last else "├── "
                lines.append(f"{indent2}{p_prefix}{rec.slug}/")

                leaf_indent = indent2 + ("    " if p_last else "│   ")
                lines.append(f"{leaf_indent}├── solution.py")
                if rec.note_rel and rec.note_rel.parent == rec.problem_rel:
                    lines.append(f"{leaf_indent}└── {rec.note_rel.name}")
                else:
                    lines.append(f"{leaf_indent}└── test_cases.txt")

    lines.append("```")
    return lines


def render_topic_sections(records: List[ProblemRecord]) -> List[str]:
    by_topic: Dict[Path, List[ProblemRecord]] = {}
    for r in records:
        by_topic.setdefault(r.topic_rel, []).append(r)

    lines: List[str] = []
    for topic_rel in sorted(by_topic.keys(), key=lambda x: x.as_posix()):
        topic_name = topic_rel.name
        topic_index = topic_rel / "index.md"
        lines.append(f"### {topic_name}")
        if topic_index.exists():
            lines.append(f"- 目录说明：{md_link('index.md', safe_rel(topic_index))}")
        lines.append("")
        lines.append("| 题目目录 | LeetCode | 本地题解 | 实现代码 |")
        lines.append("| --- | --- | --- | --- |")

        for rec in sorted(by_topic[topic_rel], key=lambda x: x.slug):
            p_link = md_link(rec.slug, safe_rel(rec.problem_rel))
            if rec.leetcode_url:
                lc = md_link("题目", rec.leetcode_url)
            else:
                lc = "待补充"

            notes: List[str] = []
            if rec.note_rel:
                notes.append(md_link("题解", safe_rel(rec.note_rel)))
            if rec.analysis_anchor:
                notes.append(md_link("分析", f"{safe_rel(topic_index)}#{rec.analysis_anchor}"))
            note = " / ".join(notes) if notes else "待补充"

            code = md_link("solution.py", safe_rel(rec.code_rel))
            lines.append(f"| {p_link} | {lc} | {note} | {code} |")
        lines.append("")
    return lines


def build_root_index(records: List[ProblemRecord]) -> str:
    lines: List[str] = []
    lines.append("# LeetCode 题解导航")
    lines.append("")
    lines.append("> 本文件由 generate_index.py 自动生成。")
    lines.append("")
    lines.append("## 子目录 index.md 约定（INDEX_FORMAT_V1）")
    lines.append("")
    lines.append("每个题型目录（如 hash、mono_stack）建议使用如下 Markdown 表格：")
    lines.append("")
    lines.append("| slug | title | leetcode | solution | code | analysis_anchor |")
    lines.append("| --- | --- | --- | --- | --- | --- |")
    lines.append("| two_sum | Two Sum | https://leetcode.com/problems/two-sum/ | ./two_sum/README.md | ./two_sum/solution.py | two_sum |")
    lines.append("")
    lines.append("说明：")
    lines.append("- slug：题目目录名（必须与文件夹一致）")
    lines.append("- title：题目标题（可中文或英文）")
    lines.append("- leetcode：LeetCode 题目 URL")
    lines.append("- solution：本地题解文档相对路径（相对于当前题型目录）")
    lines.append("- code：实现代码相对路径（相对于当前题型目录）")
    lines.append("- analysis_anchor：可选，指向当前题型 index.md 中的分析段锚点（如 two_sum）")
    lines.append("- 若 analysis_anchor 为空，但存在标题 `### <slug>`，会自动链接到该标题")
    lines.append("")
    lines.append("分析段推荐写法：")
    lines.append("- 在题型 index.md 中添加 `## 题目分析`")
    lines.append("- 每题一段，使用 `### <slug>` 作为小节标题")
    lines.append("")
    lines.append("## 题目索引")
    lines.append("")
    lines.extend(render_topic_sections(records))
    lines.append("## 文件树")
    lines.append("")
    lines.extend(render_tree(records))
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    records = build_records()
    content = build_root_index(records)
    OUTPUT_FILE.write_text(content, encoding="utf-8")
    print(f"Generated {OUTPUT_FILE} with {len(records)} problems.")


if __name__ == "__main__":
    main()
