Doctrine DBAL 2.5.3 Released
============================

We are happy to announce the immediate availability of Doctrine DBAL
`2.5.3 <https://github.com/doctrine/dbal/releases/tag/v2.5.3>`_.

The SQLServer platform support for pagination query modification was
completely rewritten, improving stability and code quality as well as
ease of maintenance. `#818 <https://github.com/doctrine/dbal/issues/818>`_

Dependency constraints on the
`doctrine/common <https://github.com/doctrine/common>`_ component supported
versions were corrected, allowing users to install ``doctrine/common``
``2.6.*`` together with the DBAL. `#2268 <https://github.com/doctrine/dbal/issues/2268>`_

Installation
~~~~~~~~~~~~

You can install the DBAL component using Composer:

.. code-block:: shell

  composer require doctrine/dbal:~2.5.3

Please report any issues you may have with the update on the
`issue tracker <https://github.com/doctrine/dbal/issues>`_.

.. author:: Marco Pivetta <ocramius@gmail.com>
.. categories:: Release
.. tags:: none
.. comments::
