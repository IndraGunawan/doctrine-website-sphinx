Cache 1.4.0 Released
====================

We are happy to announce the immediate availability of Doctrine Cache 1.4.0.

This release fixes a series of performance and compatibility issues in the
filesystem-based cache adapters (`#16 <https://github.com/doctrine/cache/pull/16>`_,
`#50 <https://github.com/doctrine/cache/pull/50>`_,
`#55 <https://github.com/doctrine/cache/pull/55>`_).

New cache adapters for ``SQlite3`` (`#32 <https://github.com/doctrine/cache/pull/32>`_)
and ``Predis`` (`#28 <https://github.com/doctrine/cache/pull/28>`_) were implemented.

A new ``ChainCache`` (`#52 <https://github.com/doctrine/cache/pull/52>`_)
was implemented, allowing multiple levels of caching, for performance and
efficiency.

New interfaces were introduced, for better interface segregation and improved performance:

- ``MultiGetCache`` (`#29 <https://github.com/doctrine/cache/pull/29>`_)
- ``FlushableCache`` (`#48 <https://github.com/doctrine/cache/pull/48>`_)
- ``ClearableCache`` (`#48 <https://github.com/doctrine/cache/pull/48>`_)

This release also causes the filesystem-based caches to change directory structure
for saved files: please clear your file-based caches completely before upgrading.

You can find the complete changelog for this release in the
`release notes <https://github.com/doctrine/cache/releases/tag/v1.4.0>`_.

You can install the Cache component using Composer and the following ``composer.json``
contents:

.. code-block:: json

  {
      "require": {
          "doctrine/cache": "1.4.0"
      }
  }

Please report any issues you may have with the update on the mailing list or on
`Jira <http://www.doctrine-project.org/jira>`_.

.. author:: Steve Müller <deeky666@googlemail.com>
.. categories:: none
.. tags:: none
.. comments::
