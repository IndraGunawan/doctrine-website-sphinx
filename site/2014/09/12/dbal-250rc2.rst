Doctrine DBAL 2.5 RC2
=====================

We are happy to announce the immediate availability of `Doctrine DBAL 2.5 RC2`_,
which fixes over 30 bugs including SQL Server LIMIT/OFFSET issues, several identifiers quotation
issues, schema introspection related issues and many more.
This release candidate also introduces some nice new features and improvements since
`Doctrine DBAL 2.5 BETA3`_:

- Support for connection flags in the mysqli driver
- Support for Spatial Indexes in MySQL
- Support date arithmetic interval methods for seconds, minutes, weeks, quarters and years
- Support for Partial Indexes in PostgreSQL and SQLite
- ``Doctrine\DBAL\Connections\MasterSlaveConnection`` can now be closed via ``close()``
- Ability to retrieve parameter types from the query builder
- Make table alias in query builder optional for simple queries

We hope this will be the last release candidate before final release and you should expect
to see the finished DBAL 2.5 very soon.

For details about all the new features in DBAL 2.5, see the `previous release
blog post <http://www.doctrine-project.org/2014/02/21/doctrine_2_5_beta3.html>`_
and the `Jira Release
<http://www.doctrine-project.org/jira/browse/DBAL/fixforversion/10523>`_.

You can install the Release Candidate through Composer with the following version
constraint:

.. code-block:: json

    {
        "require": {
            "doctrine/dbal": "2.5.0@RC"
        }
    }

DBAL 2.5 is backwards compatible to 2.4 and earlier in everything except for small
details (See ``UPGRADE.md``). You can even test Doctrine DBAL 2.5 with a stable
ORM 2.4 version.

If you find any problems with this beta, please report a bug `on Jira
<http://www.doctrine-project.org/jira>`_.

.. _Doctrine DBAL 2.5 RC2: https://github.com/doctrine/dbal/releases/tag/v2.5.0-RC2
.. _Doctrine DBAL 2.5 BETA3: https://github.com/doctrine/dbal/releases/tag/v2.5.0-BETA3
