DBAL and ORM 2.2 Release candidates
===================================

Again with a slight delay we finalized the DBAL and ORM release candidates for the 2.2 branch. There have been some late changes that made the delay necessary:

* DBAL Schema supported was heavily refactored to include the concept of "namespaces". This abstracts multi-database useage for MySQL and Schema support for PostgreSQL.
* A Paginator was put into the Doctrine\ORM\Tools\Pagination namespace. Its the combination of the original DoctrineExtensions Paginator with extensions done in the KnpLabs components and the Pagerfanta library.

As usual you can grab the code from:

* `Packagist <http://packagist.org/packages/doctrine/>`_
* `PEAR <http://pear.doctrine-project.org>`_
* `Downloads <http://www.doctrine-project.org/projects>`_
* `Github <http://github.com/doctrine>`_

Please test this code with your applications. If no bugs or backwards-compatible breaks are reported in the next days we will release the final version on friday.

.. author:: Benjamin Eberlei 
.. categories:: Release
.. tags:: none
.. comments::
