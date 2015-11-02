Cache 1.4.4 and 1.5.1 Released
==============================

We are happy to announce the immediate availability of Doctrine Cache
`1.4.4 <https://github.com/doctrine/cache/releases/tag/v1.4.4>`_ and
`1.5.1 <https://github.com/doctrine/cache/releases/tag/v1.5.1>`_.

Cache 1.4.4
~~~~~~~~~~~

This release fixes the version number reported in
`Doctrine/Common/Cache/Version::VERSION <https://github.com/doctrine/cache/blob/v1.5.1/lib/Doctrine/Common/Cache/Version.php>`_

Additionally, a flaw in ``CacheProvider#fetchMultiple()`` was fixed:
``null`` and false-y values being fetched were considered cache misses,
but are now correctly included in the results
(`#104 <https://github.com/doctrine/cache/pull/104>`_).

You can find the complete changelog for this release in the
`v1.4.4 release notes <https://github.com/doctrine/cache/releases/tag/v1.4.4>`_.

Cache 1.5.1
~~~~~~~~~~~

This release includes all the fixes mentioned in the above ``1.4.4``
patch.

You can find the complete changelog for this release in the
`v1.5.1 release notes <https://github.com/doctrine/cache/releases/tag/v1.5.1>`_.

Installation
~~~~~~~~~~~~

You can install the Cache component using Composer either of the following
``composer.json`` definitions:

.. code-block:: json

  {
      "require": {
          "doctrine/cache": "~1.4.4"
      }
  }

.. code-block:: json

  {
      "require": {
          "doctrine/cache": "~1.5.1"
      }
  }

Please report any issues you may have with the update on the mailing list or on
`Jira <http://www.doctrine-project.org/jira>`_.

.. author:: Marco Pivetta <ocramius@gmail.com>
.. categories:: Release
.. tags:: none
.. comments::
