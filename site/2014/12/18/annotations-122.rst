Annotations 1.2.2 released
==========================

We are happy to announce the immediate availability of ``doctrine/annotations`` 1.2.2.

The release includes following fixes:

- `43: Exclude files from distribution via .gitattributes <https://github.com/doctrine/annotations/pull/43>`_
- `44: Prevent stack overflows in "preg_split" in the lexer <https://github.com/doctrine/annotations/pull/44>`_
- `46: Fixed race conditions in FileCacheReader by improving I/O operations atomicity <https://github.com/doctrine/annotations/pull/46>`_
- `48: Deprecating the FileCacheReader in 1.2.2: will be removed in 2.0.0 <https://github.com/doctrine/annotations/pull/48>`_

You can install the Annotations library using Composer and the following ``composer.json``
contents:

.. code-block:: json

  {
      "require": {
          "doctrine/annotations": "1.2.2"
      }
  }

.. author:: Marco Pivetta <ocramius@gmail.com>
.. categories:: none
.. tags:: none
.. comments::
