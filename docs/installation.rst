============
Installation
============

Choose what you need
====================

**Reading an exported model:** open its HTTP/HTTPS link in a WebGL-capable
browser. You need no Python, Node.js, framework installation or CAD backend.

**Working on a Machinome model:** install the viewer into the Python environment
that runs the framework. Machinome owns modeling, builds and file watching;
the viewer displays the result. See the framework's
`quick start <https://machinome.readthedocs.io/en/latest/quickstart.html>`_
for the matching framework and CAD setup.

**Building an embedding host:** obtain ``machinome-viewer.js`` from an installed
package or a framework export, then follow :doc:`embedding`. There is no
separately published npm package to install; the browser bundle travels with
the Python distribution.

Install the current source version
==================================

Version |package-version| is not yet published on PyPI. Do not expect a
``pip install machinome-viewer==0.2.0`` command to obtain this checkout.
From an available checkout of ``machinome-viewer``, with **Python 3.11+** and
**Node.js 22+**:

.. code-block:: console

   python -m venv .venv
   . .venv/bin/activate
   npm ci --prefix machinome_viewer/widget
   npm run build --prefix machinome_viewer/widget
   python -m pip install -e .
   machinome-viewer describe

If you already have a framework environment, activate that environment instead
of creating a second one. The final command reports the installed bundle paths,
package version, API version, and supported document versions as JSON.

Once distributions are published, the intended maker installation is
``python -m pip install "machinome[viewer]"``. Built wheels and source
distributions carry the bundle: **installing a distribution needs no npm**.
Node is needed when building frontend source, not for ordinary viewing.

Open a project
==============

In a configured Machinome project using the matching framework source:

.. code-block:: console

   machinome viewer
   machinome develop

``machinome viewer`` reports the viewer the framework actually found.
``machinome develop`` builds the project's model, opens the development
viewer, and watches source changes. A project with multiple models may need
an explicit model reference; consult the framework's command help.
The usual URL is ``http://localhost:8000``.

For an existing published build directory, without a framework process:

.. code-block:: console

   machinome-viewer serve --build-dir /path/to/build --port 8000

The directory must contain ``viewer.json`` and its referenced model files.
This command **serves a build; it does not build or watch Python source**.
See :doc:`reference/cli` for its options and the development-server contract.

.. warning::

   The development server binds ``0.0.0.0`` (all interfaces) and has no
   authentication. Use it on a trusted development machine/network; do not
   expose it as a public hosting service. Publish a static export for readers.

Enable headless snapshots
=========================

In the viewer source checkout and the same Python environment:

.. code-block:: console

   python -m pip install -e ".[snapshot]"
   python -m playwright install chromium

Playwright's Python package and its Chromium installation are separate
requirements. Some Linux environments also need browser system dependencies;
follow the error's Playwright installation guidance. Interactive browser
viewing does not require this extra. See :doc:`sharing` for capture examples.
