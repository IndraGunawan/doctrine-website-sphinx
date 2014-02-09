MongoDB ODM: Query Builder API
==============================

The Doctrine MongoDB Object Document Mapper includes a fluent
object oriented API for building queries to execute against
MongoDB. Recently some changes were made to the API to simplify it
and make it more readable. This blog post aims to demonstrate and
introduce the new API to you!

Query Types
-----------

The API still supports all the types of queries you would expect:


-  `find <#find>`_
-  `insert <#insert>`_
-  `update <#update>`_
-  `delete <#delete>`_

Continue reading to see examples for each of the above types of
queries!

## Find

You can easily find documents by just creating a new ``Query``
object with the ``createQuery()`` method. A new ``Query`` object
defaults to a ``find`` query so you just need to pass the name of
the document to query for:

.. code-block:: php

    <?php
    $q = $dm->createQuery('User');

You can change the document being queried for by using the
``find()`` method:

.. code-block:: php

    <?php
    $q->find('Project');

Conditions
~~~~~~~~~~

You can limit the returned documents by specifying some
conditions:

.. code-block:: php

    <?php
    $q->field('title')->equals('The Doctrine Project');

Maybe you want to only return projects created after today:

.. code-block:: php

    <?php
    $q->field('createdAt')->greaterThan(new MongoDate(time()));

You can even a condition on an embedded document:

.. code-block:: php

    <?php
    $q->field('profile.firstName')->equals('Jonathan');

Also, you can add a condition for a referenced document to filter
by id:

.. code-block:: php

    <?php
    $q->field('account.$id')->equals($accountId);

The ``field()`` method specifies the current field to add the
conditions to. You can optionally use the magical ``__call()``
feature of the ``Query`` object to specify the current field as
well:

.. code-block:: php

    <?php
    $q->createdAt()->greaterThan(new MongoDate(time()));

All the methods you'd expect can be used in combination with the
``field()`` method for adding conditions to your query:


-  equal($value)
-  where($javascript)
-  not($value)
-  in($values)
-  notIn($values)
-  notEqual($value)
-  greaterThan($value)
-  greaterThanOrEq($value)
-  lessThan($value)
-  lessThanOrEq($value)
-  range($start, $end)
-  size($size)
-  exists($bool)
-  type($type)
-  all($values)
-  mod($mod)

## Insert

You can easily insert new documents using the ``Query`` API as
well. Just use the ``insert()`` method in combination with
``field()`` and ``set()``:

.. code-block:: php

    <?php
    $q = $dm->createQuery('User')
        ->insert()
        ->field('username')->set('jwage')
        ->field('password')->set('password');

If you want to set the new document to insert you can use the
``setNewObj()`` method:

.. code-block:: php

    <?php
    $q = $dm->createQuery('User')
        ->insert()
        ->setNewObj(array(
            'username' => 'jwage',
            'password' => 'password'
        ));

## Update

If you want to update a document you can use the ``update()``
method in combination with ``field()``, ``set()`` and conditions.
Here is an example where we create a query to update a user with
the username ``jwage`` and give him a new password:

.. code-block:: php

    <?php
    $q = $dm->createQuery('User')
        ->update()
        ->field('password')->set('newpassword')
        ->field('username')->equals('jwage');

## Delete

You can delete documents as well by using the ``delete()`` method
in combination with conditions. Here is an example where we create
a query to delete the user document with a username of ``jwage``:

.. code-block:: php

    <?php
    $q = $dm->createQuery('User')
        ->delete()
        ->field('username')->equals('jwage');

As you can see the fluent API makes it a bit easier to express
queries that are easy to read in the same way you would read
english from left to right. We hope to enhance and improve this API
even more before we release the stable 1.0 version.

You can read more about the Query Builder API in the
`documentation <http://www.doctrine-project.org/projects/mongodb_odm/1.0/docs/reference/query-builder-api/en#query-builder-api>`_.



.. author:: jwage 
.. categories:: none
.. tags:: none
.. comments::
