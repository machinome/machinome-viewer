================
Machinome Viewer
================

**Inspect a machine. Move its inputs. See how it works.**

Machinome Viewer is the browser viewer for the
`Machinome framework <https://machinome.readthedocs.io/>`_. It turns a
published model into an interactive 3D assembly: orbit the camera, look inside
subassemblies, operate declared controls, and watch the machine respond.

Use it through ``machinome develop``, share a self-contained export, or embed
the same viewer in your own page. The browser reads the model's published
geometry and mechanical relationships; it does not need Python or a CAD
backend to display and operate an export.

.. note::

   The 0.7.0 baseline, recorded on 23 September 2026 alongside Machinome
   0.7.0, declares viewer API |baseline-viewer-api| and reads document
   versions |baseline-document-versions|. This source checkout's additional
   capability is identified in :doc:`compatibility`; its installation can
   report the exact bundle it carries. :doc:`installation` explains setup.

Start here
==========

* **Opening a model?** :doc:`Install the viewer <installation>`, then learn
  :doc:`how to inspect and operate a machine <using-the-viewer>`.
* **Sharing your work?** :doc:`Publish an export or take a snapshot <sharing>`.
* **Building a host?** Follow the :doc:`working embedding example <embedding>`
  and the :doc:`browser API reference <reference/index>`.
* **Authoring the mechanics?** Use the `framework manual
  <https://machinome.readthedocs.io/>`_ and `mechanics helper reference
  <https://machinome-mechanics.readthedocs.io/>`_. The viewer consumes those
  models; it does not define their CAD or mechanical laws.

Try the viewer
==============

This small spinner is a real, committed export: a red hub and three blue
blades driven by the animation timeline. Load it, drag to orbit, scroll to
zoom, or open **Assembly** to focus and hide parts. It is a posed model,
not a running simulation.

.. raw:: html

   <div class="viewer-demo">
     <button type="button" data-viewer-demo="examples/embed.html">Load interactive spinner</button>
     <p>The example runs locally in your browser. No CAD service or account is needed.</p>
   </div>

The :doc:`embedding guide <embedding>` includes the complete source for this
example. A WebGL-capable browser is required; the rest of this manual works
without loading it.

One viewer, several homes
============================

The same bundle powers the development page, portable export page, custom
embeds, and headless capture. The Python package provides the development
server and capture command. It is **AGPL-3.0-only**, separate from the
Apache-2.0 Machinome framework, which reaches it through a small lookup and
separate processes. Neither package imports the other's runtime.

.. toctree::
   :maxdepth: 1
   :caption: User guide

   installation
   using-the-viewer
   sharing
   embedding
   compatibility
   troubleshooting

.. toctree::
   :maxdepth: 2
   :caption: Reference

   reference/index

.. toctree::
   :caption: Machinome ecosystem

   Framework manual <https://machinome.readthedocs.io/>
   Mechanics helpers <https://machinome-mechanics.readthedocs.io/>
   Source code <https://github.com/machinome/machinome-viewer>
