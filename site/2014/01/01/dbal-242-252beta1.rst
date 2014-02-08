DBAL 2.4.2 and 2.5.0 BETA1 released
===================================

*Published: 01.01.2014*

We are happy to announce the immediate availability of Doctrine DBAL 2.4.2 and
2.5.0 BETA1.

The new stable version 2.4.2 had 20 bugs fixed. You can install this version
using Composer and the following ``composer.json`` contents:

.. code-block:: json

    {
        "require": {
            "doctrine/dbal": "2.4.2"
        }
    }

You can see all the changes on Jira:

- `DBAL 2.4.2
  <http://www.doctrine-project.org/jira/browse/DBAL/fixforversion/10620>`_

In the first 10 month of 2013 we watched the number of open issues cross 100
and peak at 250 in mid November, unable to do much about it due to time
constraints. During the last two months however we have worked hard to lower
the number of open pull-requests on DBAL from 50 to only 7 and push the number
of open issues on DBAL+ORM down to 188 from 250. This has been a tremendous
effort and it would not have been possible without our two new core team members
`deeky666 <https://github.com/deeky666>`_ and `kimhemsoe
<https://github.com/kimhemsoe>`_.

With the number of open bugs at 22 and open pull requests at 7 I am excited
to say that DBAL 2.5 will be the most stable and complete version so far. It
is mostly backwards compatible with only some minor changes necessary, when
using PDO IBM, creating a custom platform or using non-default DateTime
formats. You can see the breaks in the `UPGRADE.md
<https://github.com/doctrine/dbal/blob/master/UPGRADE.md>`_ file.

There is also a nice list of new features:

- Support for SAP Sybase SQL Anywhere versions 10, 11, 12 and 16 (DBAL-475)
- Support for auto-commit=NO on all drivers and platforms. (DBAL-81)
- Refactor exceptions to use common error-codes and exception classes that
  derive from ``Doctrine\DBAL\DBALException``. (DBAL-407)
- Add support to retry connections with ``Doctrine\DBAL\Connection#ping()``
  method. (DBAL-275)
- Add INSERT support to QueryBuilder (DBAL-320)
- Add Binary type for VARBINARY support (DBAL-714)
- Add charset and SSL connection support to PostgreSQL (DBAL-567, DBAL-702)
- Add options support for Myqli (DBAL-643)

See all the changes for the 2.5.0 BETA1 on Jira:

- `DBAL 2.5.0 BETA1
  <http://www.doctrine-project.org/jira/browse/DBAL/fixforversion/10523>`_

You can install the BETA using Composer and the following ``composer.json``
contents:

.. code-block:: json

    {
        "require": {
            "doctrine/dbal": "2.5.0-BETA1"
        }
    }

.. author:: Benjamin Eberlei <kontakt@beberlei.de>
.. categories:: none
.. tags:: none
.. comments::
