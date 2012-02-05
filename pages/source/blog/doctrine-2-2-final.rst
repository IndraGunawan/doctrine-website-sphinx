:date: 2012-01-29 10:10:10
:author: Benjamin Eberlei <kontakt@beberlei.de>

=====================
Doctrine 2.2 released
=====================

We released Doctrine 2.2 today. 

A top list of the new features includes:

* Filtering entities and associations based on rules that can be parameterized, enabled or disabled, developed by asm89
* Support for complex SQL types such as Geometries, IPs, develped by jsor.
* Bit Comparisions in DQL, developed by Fabio.
* Annotation Refactorings by Fabio and johannes.
* DQL Refactoring, ORDER BY and GROUP BY supporting result variables of SELECT expressions.
* Alias for entities in DQL results.
* Result Cache refactoring
* Flush for single entities
* Master/Slave Connection in DBAL

See the changelogs of all three projects Common, DBAL, ORM:

* `ORM <http://www.doctrine-project.org/jira/browse/DDC/fixforversion/10157>`_
* `DBAL <http://www.doctrine-project.org/jira/browse/DBAL/fixforversion/10142>`_
* `Common <http://www.doctrine-project.org/jira/browse/DCOM/fixforversion/10152>`_

See the `UPGRADE_2_2 <https://github.com/doctrine/doctrine2/blob/master/UPGRADE_TO_2_2>`_ file to see backwards incompatible changes.

You can install the release through `Github <https://github.com/doctrine/doctrine2>`_, `PEAR <http://pear.doctrine-project.org>`_ or through `Composer <http://www.packagist.org>`_:

    {
        "require":
        {
            "doctrine/orm": "2.2.0"
        }
    }
