Annotations 1.2.3 released
==========================

We are happy to announce the immediate availability of ``doctrine/annotations`` 1.2.3.

The release includes fixes for regressions that were introduced by some bug-fixes
in version 1.2.2:

- `49: #46 - applying correct chmod() to generated cache file <https://github.com/doctrine/annotations/pull/49>`_
- `50: Hotfix: match escaped quotes (revert #44) <https://github.com/doctrine/annotations/pull/50>`_

You can install the Annotations library using Composer and the following ``composer.json``
contents:

.. code-block:: json

  {
      "require": {
          "doctrine/annotations": "1.2.3"
      }
  }

.. author:: Marco Pivetta <ocramius@gmail.com>
.. categories:: none
.. tags:: none
.. comments::
