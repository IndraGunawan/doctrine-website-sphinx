DBAL 2.3.5 released
===================

We are happy to announce the immediate availability of Doctrine DBAL 2.3.5, which fixes a
minor issue introduced in 2.3.4 where ``null`` parameter values passed to one of the connection
execution methods led to an error.

You can find all the changes on JIRA:

- `DBAL 2.3.5 <http://www.doctrine-project.org/jira/browse/DBAL/fixforversion/10721>`_ - 8 issues fixed

You can install the DBAL using Composer and the following ``composer.json``
contents:

.. code-block:: json

  {
      "require": {
          "doctrine/dbal": "2.3.5"
      }
  }

Please report any issues you may have with the update on the mailing list or on
`Jira <http://www.doctrine-project.org/jira>`_.

.. author:: Steve Müller <deeky666@googlemail.com>
.. categories:: none
.. tags:: none
.. comments::
