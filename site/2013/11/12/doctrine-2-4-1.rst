Doctrine 2.4.1 released
=======================

Today we released Doctrine DBAL 2.4.1 and ORM 2.4.1 versions.
It includes an important fix for a regression with array hydration.
In total 6 tickets have been closed in both releases.

See all the changes:

- `Doctrine ORM v2.4.1 Changelog
  <http://www.doctrine-project.org/jira/browse/DDC/fixforversion/10528>`_
- `Doctrine DBAL v2.4.1 Changelog
  <http://www.doctrine-project.org/jira/browse/DBAL/fixforversion/10527>`_

Installation
------------

You can install Doctrine using Composer and the following ``composer.json``
contents:

.. code-block:: json

    {
        "require": {
            "doctrine/common": "2.4.*",
            "doctrine/dbal": "2.4.1",
            "doctrine/orm": "2.4.1"
        }
    }

.. author:: Benjamin Eberlei 
.. categories:: Release
.. tags:: none
.. comments::
