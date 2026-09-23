"""A standalone user manual: no viewer runtime, framework or CAD imports."""

import json
import os
from pathlib import Path
import shutil
import tomllib

from sphinx.errors import ExtensionError

ROOT = Path(__file__).resolve().parents[1]
WIDGET = ROOT / "machinome_viewer" / "widget"
BUNDLE = WIDGET / "dist" / "machinome-viewer.js"
metadata = tomllib.loads((ROOT / "pyproject.toml").read_text())["project"]
widget = json.loads((WIDGET / "package.json").read_text())

project = "Machinome Viewer"
author = "Luis Henrique Cassis Fagundes"
copyright = "2023–2026, Luis Henrique Cassis Fagundes"
release = metadata["version"]
version = release
extensions = []
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
nitpicky = True
highlight_language = "javascript"
rst_prolog = (
    f".. |package-version| replace:: {release}\n"
    f".. |viewer-api| replace:: {widget['machinomeViewerApi']}\n"
    ".. |document-versions| replace:: "
    + ", ".join(map(str, widget["machinomeDocumentVersions"])) + "\n"
    ".. |baseline-viewer-api| replace:: 25\n"
    ".. |baseline-document-versions| replace:: 1 through 12\n"
)

html_theme = "sphinx_rtd_theme"
html_title = f"{project} — The browser viewer for Machinome"
html_static_path = ["_static"]
html_css_files = ["viewer-docs.css"]
html_js_files = ["demo.js"]
html_theme_options = {
    "navigation_depth": 2,
    "collapse_navigation": False,
    "style_external_links": True,
}
html_context = {
    "display_github": True,
    "github_user": "machinome",
    "github_repo": "machinome-viewer",
    "github_version": "main",
    "conf_py_path": "/docs/",
}
html_baseurl = os.environ.get(
    "READTHEDOCS_CANONICAL_URL",
    "https://machinome-viewer.readthedocs.io/en/latest/",
)


def require_bundle(app):
    if app.builder.format != "html":
        return
    inputs = [WIDGET / name for name in ("package.json", "build.mjs", "tsconfig.json")]
    inputs.extend(path for path in (WIDGET / "src").rglob("*") if path.is_file())
    if not BUNDLE.is_file() or any(
        path.stat().st_mtime_ns > BUNDLE.stat().st_mtime_ns for path in inputs
    ):
        raise ExtensionError(
            "Build the current documentation demo first: "
            "npm ci --prefix machinome_viewer/widget && "
            "npm run build --prefix machinome_viewer/widget"
        )


def copy_examples(app, exception):
    if exception is not None or app.builder.format != "html":
        return
    target = Path(app.outdir) / "examples"
    shutil.copytree(ROOT / "docs" / "examples", target, dirs_exist_ok=True)
    shutil.copytree(ROOT / "tests" / "fixtures" / "spinner", target / "spinner", dirs_exist_ok=True)
    shutil.copy2(BUNDLE, target / "machinome-viewer.js")


def setup(app):
    app.connect("builder-inited", require_bundle)
    app.connect("build-finished", copy_examples)
    return {"parallel_read_safe": True, "parallel_write_safe": True}
