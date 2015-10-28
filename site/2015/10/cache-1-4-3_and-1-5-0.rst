Cache 1.4.3 and 1.5.0 Released
==============================

We are happy to announce the immediate availability of Doctrine Cache
`1.4.3 <https://github.com/doctrine/cache/releases/tag/v1.4.3>`_ and
`1.5.0 <https://github.com/doctrine/cache/releases/tag/v1.5.0>`_.

Cache 1.4.3
~~~~~~~~~~~

This release fixes some minor issues that prevented various cache adapters
from correctly reporting success or failure in case of cache key deletion
(`#95 <https://github.com/doctrine/cache/pull/95>`_).

Another issue being fixed is related to ``CacheProvider#fetchMultiple()``,
which was failing to operate when an empty list was given to it
(`#90 <https://github.com/doctrine/cache/pull/90>`_).

Also, the ``CacheProvider`` does not store version information internally
unless ``CacheProvider#deleteAll()`` was called at least once
(`#91 <https://github.com/doctrine/cache/pull/91>`_).

You can find the complete changelog for this release in the
`v1.4.3 release notes <https://github.com/doctrine/cache/releases/tag/v1.4.3>`_.

Cache 1.5.0
~~~~~~~~~~~

This release includes all the changes released with version 1.4.3, as well
as further bug fixes and improvements that will require you to clean your
caches (if file-based) during the upgrade.

PHP7 support is now guaranteed (`#92 <https://github.com/doctrine/cache/pull/92>`_).

File based caches now use a much lower number of directories
(`#94 <https://github.com/doctrine/cache/pull/94>`_).

Proper support for wincache multi-get was added
(`#97 <https://github.com/doctrine/cache/pull/97>`_).

Predis cache adapter now relies on the ``Predis\ClientInterface``
(`#87 <https://github.com/doctrine/cache/pull/87>`_).

You can find the complete changelog for this release in the
`v1.5.0 release notes <https://github.com/doctrine/cache/releases/tag/v1.5.0>`_.

Credits
~~~~~~~

We would like to thank all contributors that patiently supported us
in fixing the file-based cache directory structure long-standing issues,
and especially:

 - Tobias `Tobion <https://github.com/Tobion>`_ Schultze
 - Krzysztof `Crozin <https://github.com/Crozin>`_ Łabuś
 - Steve `kamermans <https://github.com/kamermans>`_ Kamerman

Installation
~~~~~~~~~~~~

You can install the Cache component using Composer either of the following
``composer.json`` definitions:

.. code-block:: json

  {
      "require": {
          "doctrine/cache": "~1.4.1"
      }
  }

.. code-block:: json

  {
      "require": {
          "doctrine/cache": "~1.5.0"
      }
  }

Please report any issues you may have with the update on the mailing list or on
`Jira <http://www.doctrine-project.org/jira>`_.

.. author:: Marco Pivetta <ocramius@gmail.com>
.. categories:: Release
.. tags:: none
.. comments::
