"""Verify the installed package and the foundation's internal dependency direction."""

import ast
import os
import subprocess
import sys
from graphlib import TopologicalSorter
from importlib.util import resolve_name
from pathlib import Path


def test_installed_package_from_outside_checkout(tmp_path):
    command = """
import importlib
import pkgutil
import macroswing
modules = {m.name for m in pkgutil.walk_packages(macroswing.__path__, 'macroswing.')}
expected = 'core data_sources market macro technical sector patterns fundamentals news speech strategies backtesting mcp_server agents harness evidence risk memory'.split()
assert {'macroswing.' + name for name in expected} <= modules
for name in sorted(modules):
    importlib.import_module(name)
"""
    env = dict(os.environ)
    env.pop("PYTHONPATH", None)
    subprocess.run([sys.executable, "-I", "-c", command], cwd=tmp_path, env=env, check=True)


def test_foundation_import_direction():
    src = Path(__file__).resolve().parents[1] / "src" / "macroswing"
    graph = TopologicalSorter()
    for file in src.rglob("*.py"):
        parts = list(file.relative_to(src.parent).with_suffix("").parts)
        is_package = parts[-1] == "__init__"
        if is_package:
            parts.pop()
        name = ".".join(parts)
        package = name if is_package else name.rpartition(".")[0]
        dependencies = set()
        for node in ast.walk(ast.parse(file.read_text())):
            if isinstance(node, ast.Import):
                dependencies.update(alias.name for alias in node.names)
            elif isinstance(node, ast.ImportFrom):
                target = resolve_name("." * node.level + (node.module or ""), package)
                dependencies.add(target)
                dependencies.update(f"{target}.{alias.name}" for alias in node.names)
        internal = {dep for dep in dependencies if dep.startswith("macroswing.")}
        if name.startswith("macroswing.core"):
            assert all(dep.startswith("macroswing.core") for dep in internal)
        graph.add(name, *(internal - {name}))
    # Cycles raise CycleError even when Python would tolerate a partial import.
    assert tuple(graph.static_order())
