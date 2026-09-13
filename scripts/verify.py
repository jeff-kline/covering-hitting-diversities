#!/usr/bin/env python3
"""Verify a Git checkout or extracted release archive; no third-party packages."""
import hashlib
from pathlib import Path
import re
import subprocess

root = Path(__file__).resolve().parents[1]
def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()
def require(ok, message):
    if not ok:
        raise SystemExit("FAIL: " + message)
def read_hashes(path):
    entries = {}
    for line in path.read_text().splitlines():
        match = re.fullmatch(r"([0-9a-f]{64})  (.+)", line)
        require(match is not None, "malformed hash record: " + str(path.name))
        expected, name = match.groups()
        require(name not in entries, "duplicate hash entry: " + name)
        require(not Path(name).is_absolute() and '..' not in Path(name).parts,
                "unsafe hash path: " + name)
        entries[name] = expected
    return entries

def proof_region(text):
    start, end = r"\section{Definitions and construction}", r"\paragraph{Status.}"
    require(text.count(start) == text.count(end) == 1, "unique proof-region boundaries")
    require(text.index(start) < text.index(end), "ordered proof-region boundaries")
    return text.split(start, 1)[1].split(end, 1)[0]
current = (root / "paper/main.tex").read_text()
old = (root / "audit/p07/cold/PAPER.tex").read_text()
require(proof_region(current) == proof_region(old), "P07 proof region differs; reopen relevant audits")
seals = read_hashes(root / "audit/p07/cold/INITIAL-SEAL.sha256")
expected_seals = {"rounds/p07/cold/INITIAL.md", "rounds/p07/cold/CLAIMS.md"}
require(set(seals) == expected_seals, "exactly two expected original initial seals")
for name, expected in seals.items():
    path = root / "audit/p07" / name[len("rounds/p07/"):]
    require(digest(path) == expected, "initial seal: " + name)
items = re.findall(r"\\bibitem\{([^}]+)\}", current)
cites = set()
for group in re.findall(r"\\cite(?:\[[^]]*\])?\{([^}]+)\}", current):
    cites.update(x.strip() for x in group.split(','))
require(len(items) == len(set(items)) == 14 and set(items) == cites, "citation bijection")
entries = read_hashes(root / "MANIFEST.sha256")
in_git = (root / ".git").exists()
if in_git:
    files = set(subprocess.check_output(["git", "ls-files"], cwd=root, text=True).splitlines())
else:
    files = {str(p.relative_to(root)) for p in root.rglob('*') if p.is_file()
             and p.relative_to(root).parts[0] != 'build'
             and '__pycache__' not in p.relative_to(root).parts and p.name != '.DS_Store'}
require(set(entries) == files - {"MANIFEST.sha256"}, "manifest file coverage")
for name, expected in entries.items():
    path = root / name
    require(path.is_file() and not path.is_symlink(), "missing/nonregular artifact: " + name)
    require(digest(path) == expected, "manifest hash: " + name)
if in_git:
    subprocess.run(["git", "diff", "--check"], cwd=root, check=True)
    subprocess.run(["git", "diff", "--cached", "--check"], cwd=root, check=True)
print("PASS: unchanged P07 proof region, two initial seals, 14/14 citations, %d manifest entries" % len(entries))
print("Mode: " + ("Git checkout (tracked coverage and staged/unstaged whitespace)" if in_git
                   else "extracted archive (file coverage; no Git history or whitespace check)"))
print("Scope: artifact integrity and source continuity; not mathematical proof verification")
