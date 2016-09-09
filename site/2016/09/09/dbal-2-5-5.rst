Doctrine DBAL 2.5.5 Released
============================

We are happy to announce the immediate availability of Doctrine DBAL
`2.5.5 <https://github.com/doctrine/dbal/releases/tag/v2.5.5>`_.

This release contains a huge amount of fixes, specifically:

 - Parsing of SQL strings containing single quotes `#842 <https://github.com/doctrine/common/pull/842>`_
 - Listing foreign key names when no DB name is used (use current DB instead) `#856 <https://github.com/doctrine/common/pull/856>`_
 - Verifying if table names correspond on dropped foreign keys `#861 <https://github.com/doctrine/common/pull/861>`_
 - Quoting identifiers in ``DROP`` DDL statements `#862 <https://github.com/doctrine/common/pull/862>`_
 - Removing leading slash from database/schema names when using DSNs `#863 <https://github.com/doctrine/common/pull/863>`_
 - Stopped using ``template1`` as default database in Postgres `#2279 <https://github.com/doctrine/common/pull/2279>`_
 - Allowing ``"path"`` instead of ``"dbname"`` in SQLite connections `#2267 <https://github.com/doctrine/common/pull/2267>`_
 - Correcting DB2 boolean columns schema introspection `#2277 <https://github.com/doctrine/common/pull/2277>`_
 - Correcting OCI8 parameter binding, which was broken by upgrading to PHP 7.0 `#2434 <https://github.com/doctrine/common/pull/2434>`_
 - Quoting reserved table names when using ``TRUNCATE`` `#2270 <https://github.com/doctrine/common/pull/2270>`_
 - Fixing of DSN parsing when no schema is in the path `#2287 <https://github.com/doctrine/common/pull/2287>`_
 - Correcting query builder, which was adding a ``FROM`` clause even with no arguments for it `#2292 <https://github.com/doctrine/common/pull/2292>`_
 - Correcting altering primary key with ``AUTO_INCREMENT`` on MySQL (requires dropping/re-adding PK) `#2303 <https://github.com/doctrine/common/pull/2303>`_
 - Moving DB2 pagination (query modification) offset/limit count result to the end of the results `#2310 <https://github.com/doctrine/common/pull/2310>`_
 - Handling ``Throwable`` exceptions thrown in ``Connection#transactional()`` `#2390 <https://github.com/doctrine/common/pull/2390>`_
 - Correcting logging of parameters passed to a statement via ``bindParam()``  `#2440 <https://github.com/doctrine/common/pull/2440>`_
 - Allowing installation of ``symfony/console:^3.0`` `#2484 <https://github.com/doctrine/common/pull/2484>`_
 - Correcing MySQLi statements, which were returning ``null`` instead of ``false`` on no results `#2497 <https://github.com/doctrine/common/pull/2497>`_

Installation
~~~~~~~~~~~~

You can install the DBAL component using Composer:

.. code-block:: shell

  composer require doctrine/dbal:^2.5.5

Please report any issues you may have with the update on the
`issue tracker <https://github.com/doctrine/dbal/issues>`_.

.. author:: Marco Pivetta <ocramius@gmail.com>
.. categories:: Release
.. tags:: none
.. comments::
