Doctrine DBAL 2.5.2 released
============================

We are happy to announce the immediate availability of Doctrine DBAL 2.5.2.

This version fixes a regression where dropping a database on PostgreSQL didn't work properly anymore
as well as several other issues.

You can find all the changes on JIRA:

- `DBAL 2.5.2 <http://www.doctrine-project.org/jira/browse/DBAL/fixforversion/10731>`_ - 24 issues fixed

You can install the DBAL using Composer and the following ``composer.json``
contents:

.. code-block:: json

  {
      "require": {
          "doctrine/dbal": "2.5.2"
      }
  }

Please report any issues you may have with the update on the mailing list or on
`Jira <http://www.doctrine-project.org/jira>`_.

.. author:: Steve Müller <deeky666@googlemail.com>
.. categories:: none
.. tags:: none
.. comments::
