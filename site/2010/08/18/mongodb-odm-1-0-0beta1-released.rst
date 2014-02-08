MongoDB ODM 1.0.0BETA1 Released
===============================

Today I am happy to tell you we have released the first beta
version of the MongoDB Object Document Mapper. It contains many
fixes and general improvements across the code.

We fixed lots of things reported by our users in Jira but also made
lots of other improvements like improving the use of atomic
operators. Read on for a complete list of the issues fixed in
Jira:

Fixed Jira Issues
-----------------


.. raw:: html

   <ul>
   <li>
   
[MODM-32] - dbref $id persisted as string instead of objectid

.. raw:: html

   </li>
   <li>
   
[MODM-33] - Class-level annotations are ignored if set on
MappedSuperclass

.. raw:: html

   </li>
   <li>
   
[MODM-34] - Custom Id always gets sent with changeset

.. raw:: html

   </li>
   <li>
   
[MODM-35] - Proxy item gets reset on persistent collection load if
that item was in the collection

.. raw:: html

   </li>
   <li>
   
[MODM-36] - Embedded relations are not persisted after a flush()

.. raw:: html

   </li>
   <li>
   
[MODM-37] - Problems with EmbedMany and discrimatorMap and
discriminatorField

.. raw:: html

   </li>
   <li>
   
[MODM-38] - Using YAML description with embedMany causes PHP notice
error

.. raw:: html

   </li>
   <li>
   
[MODM-41] - Hydration down not work for annotation "@ReferenceMany"

.. raw:: html

   </li>
   <li>
   
[MODM-42] - PersistentCollection fails when working with
MongoGridFs

.. raw:: html

   </li>
   <li>
   
[MODM-45] - Doctrine doesn't persist empty objects

.. raw:: html

   </li>
   <li>
   
[MODM-46] - @AlsoLoad annotation causes exception when used
together with Embed/Reference annotations

.. raw:: html

   </li>
   <li>
   
[MODM-47] - @AlsoLoad annotation, used on method causes fatal error

.. raw:: html

   </li>
   <li>
   
[MODM-48] - Embedded document changes are ignored if it was empty
before

.. raw:: html

   </li>
   <li>
   
[MODM-49] - Getting PHP notice and warning with empty persistent
collection

.. raw:: html

   </li>
   <li>
   
[MODM-50] - GridFs file classes don't support inheritance

.. raw:: html

   </li>
   <li>
   
[MODM-43] - Explicit schema migration

.. raw:: html

   </li>
   <li>
   
[MODM-40] - Move value scalarization and comparison to Unit Of Work

.. raw:: html

   </li>
   </ul>
   
Download
--------

You can directly download the PEAR package file
`here <http://www.doctrine-project.org/downloads/DoctrineMongoDBODM-1.0.0BETA1.tgz>`_.
You can manually extract the code or you can install the PEAR
package file locally.

::

    $ pear install /path/to/DoctrineMongoDBODM-1.0.0BETA1.tgz

Checkout from github
~~~~~~~~~~~~~~~~~~~~

::

    $ git clone git://github.com/doctrine/mongodb-odm.git mongodb_odm
    $ cd mongodb_odm
    $ git checkout 1.0.0BETA1

Install via PEAR
~~~~~~~~~~~~~~~~

::

    $ pear install pear.doctrine-project.org/DoctrineMongoDBODM-1.0.0BETA1



.. author:: jwage <jonwage@gmail.com>
.. categories:: none
.. tags:: none
.. comments::
