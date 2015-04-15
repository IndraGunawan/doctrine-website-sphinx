Cache 1.4.1 Released
====================

We are happy to announce the immediate availability of Doctrine Cache 1.4.1.

This release fixes a series of bugs related with ``null``, ``false`` or truncated data
in the ``SQLite3`` and ``Memcache`` adapters (`#62 <https://github.com/doctrine/cache/pull/62>`_,
`#65 <https://github.com/doctrine/cache/pull/65>`_,
`#67 <https://github.com/doctrine/cache/pull/67>`_).

Improvements have been made to reduce the ``SQLite3`` cache adapter
memory usage (`#64 <https://github.com/doctrine/cache/pull/64>`_).

Also, if you use an opcode cache such as OPCache (available since PHP 5.5), you will
get major performance improvements in read operations in the ``PhpFileCache``,
which shouldn't cause any stat calls at all now (`#69 <https://github.com/doctrine/cache/pull/69>`_).

Multi-get support was built into the ``Redis`` adapter (`#60 <https://github.com/doctrine/cache/pull/60>`_).

A new ``VoidCache`` adapter has been introduced - useful for testing (`#61 <https://github.com/doctrine/cache/pull/61>`_).

You can find the complete changelog for this release in the
`release notes <https://github.com/doctrine/cache/releases/tag/v1.4.1>`_.

You can install the Cache component using Composer and the following ``composer.json``
contents:

.. code-block:: json

  {
      "require": {
          "doctrine/cache": "1.4.1"
      }
  }

Please report any issues you may have with the update on the mailing list or on
`Jira <http://www.doctrine-project.org/jira>`_.

.. author:: Marco Pivetta <ocramius@gmail.com>
.. categories:: Release
.. tags:: none
.. comments::
