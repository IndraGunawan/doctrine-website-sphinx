Common 2.5.2 and 2.6.0 Released
===============================

We are happy to announce the immediate availability of Doctrine Common
`2.5.2 <https://github.com/doctrine/common/releases/tag/v2.5.2>`_ and
`2.6.0 <https://github.com/doctrine/common/releases/tag/v2.6.0>`_.

Common 2.5.2
~~~~~~~~~~~~

``chmod()`` warnings caused by proxy generation are now silenced
`#383 <https://github.com/doctrine/common/pull/383>`_
`DCOM-299 <http://www.doctrine-project.org/jira/browse/DCOM-299>`_.

``SymfonyFileLocator#getAllClassNames()`` was dropping some classes: now fixed
`#384 <https://github.com/doctrine/common/pull/384>`_
`DCOM-301 <http://www.doctrine-project.org/jira/browse/DCOM-301>`_.

Corrected fatal error triggered by ``AbstractManagerRegistry#getManagerForClass()``
when no parent class is found for a proxy
`#387 <https://github.com/doctrine/common/pull/387>`_
`DCOM-303 <http://www.doctrine-project.org/jira/browse/DCOM-303>`_.

You can find the complete changelog for this release in the
`v2.5.2 release notes <http://www.doctrine-project.org/jira/projects/DCOM/versions/10820>`_.

Common 2.6.0
~~~~~~~~~~~~

This release includes all of the fixes reported above for 2.5.2, as well
as following changes:

Proxy generation now supports PHP 7.0+ scalar type hints and return types
`#376 <https://github.com/doctrine/common/pull/376>`_
`DCOM-294 <http://www.doctrine-project.org/jira/browse/DCOM-294>`_.

Switched autoloading to PSR-4
`#389 <https://github.com/doctrine/common/pull/389>`_
`DCOM-305 <http://www.doctrine-project.org/jira/browse/DCOM-305>`_.

Added a ``.gitattributes`` to the repositories, reducing the size of the
package that is installed by composer
`#380 <https://github.com/doctrine/common/pull/380>`_
`DCOM-296 <http://www.doctrine-project.org/jira/browse/DCOM-296>`_.

You can find the complete changelog for this release in the
`v2.6.0 release notes <http://www.doctrine-project.org/jira/projects/DCOM/versions/10735>`_.

Installation
~~~~~~~~~~~~

You can install the Common component using Composer and one of the following
``composer.json`` definitions:

.. code-block:: json

  {
      "require": {
          "doctrine/common": "~2.5.2"
      }
  }

.. code-block:: json

  {
      "require": {
          "doctrine/common": "~2.6.01"
      }
  }

Please report any issues you may have with the update on the mailing list or on
`Jira <http://www.doctrine-project.org/jira>`_.

.. author:: Marco Pivetta <ocramius@gmail.com>
.. categories:: Release
.. tags:: none
.. comments::
