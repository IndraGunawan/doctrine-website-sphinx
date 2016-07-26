Doctrine Data-Fixtures 1.2.0 Released
=====================================

We are happy to announce the immediate availability of Doctrine Data-Fixtures
`1.2.0 <https://github.com/doctrine/data-fixtures/releases/tag/v1.2.0>`_.

This release fixes an issue that prevented further development of ``doctrine/orm``,
since an internal class of the ORM was used inside the ``doctrine/data-fixtures``
package. This issue is now solved by implementing a custom
```TopologicalSorter`` <https://github.com/doctrine/data-fixtures/blob/v1.2.0/lib/Doctrine/Common/DataFixtures/Sorter/TopologicalSorter.php>`_
in the library. `#222 <https://github.com/doctrine/data-fixtures/pull/222>`_

Additionally an issue with double escaping caused issues when deleting from tables
with quoted names. `#221 <https://github.com/doctrine/data-fixtures/pull/221>`_

Please also be aware that this release drops support for PHP 5.5 and below.
Given that PHP 5.5 is going to exit its official
`security support schedule <http://php.net/supported-versions.php>`_ very soon,
we strongly recommend that all users upgrade their PHP installations as well.

Installation
~~~~~~~~~~~~

You can install the ORM component using Composer:

.. code-block:: shell

  composer require doctrine/data-fixtures:^1.2.0

Please report any issues you may have with the update on the
`issue tracker <https://github.com/doctrine/data-fixtures/issues>`_.

.. author:: Marco Pivetta <ocramius@gmail.com>
.. categories:: Release
.. tags:: none
.. comments::
