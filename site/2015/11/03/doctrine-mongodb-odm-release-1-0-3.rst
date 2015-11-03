Doctrine MongoDB ODM release 1.0.3
==================================

We are happy to announce the immediate availability of Doctrine MongoDB ODM
`1.0.3 <https://github.com/doctrine/cache/releases/tag/v1.0.3>`__.

Reusing embedded documents
--------------------------

Until now, we have advised developers to deep clone embedded documents when
changing owning documents; otherwise,
`strange <https://github.com/doctrine/mongodb-odm/issues/1229`__
`things <https://github.com/doctrine/mongodb-odm/issues/1169>`__
`could <https://github.com/doctrine/mongodb-odm/issues/478>`__
`happen <https://www.youtube.com/watch?v=dQw4w9WgXcQ>`__. The reason being
was that in order for ODM to properly track changes, it would store parent
parent associations and manage the lifecycle of each document (top-level and
embedded alike). It was therefore reasonable that Doctrine require relocated
objects to be distinct instances.

*Manual cloning is no longer needed!*

With this relase, ODM will now do all the heavy lifting for you. Documents
found to have been resused during a ``persist`` or ``flush`` lifecycle event
shall be cloned by ``UnitOfWork`` automatically and updated on the parent
document or collection.

Other bug fixes
---------------

Notable fixes may be found in the
`changelog <https://github.com/doctrine/mongodb-odm/blob/master/CHANGELOG-1.0.md#103-2015-11-03>`__.
A full list of issues and pull requests included in this release may be found
in the
`1.0.3 milestone <https://github.com/doctrine/mongodb-odm/issues?q=milestone%3A1.0.3>`__.

Work on 1.1 is starting and it will require PHP 5.5+
----------------------------------------------------

We are happy to announce that work on 1.1 is commencing! While no release dates
have been scheduled, you can take a look at the
`1.1 milestone <https://github.com/doctrine/mongodb-odm/issues?q=milestone%3A1.1>`__
for brief list of goodies that we intend to ship next. If you would like to
suggest additional features or, better yet, help in with development, please
get in touch. Currently, we are looking forward to implementing
`hydrated aggregation results <https://github.com/doctrine/mongodb-odm/pull/1263>`__,
support especially now that MongoDB announced
`$lookup operator <https://www.mongodb.com/blog/post/revisiting-usdlookup>`__,
available for everybody in 3.2 and
`custom collection classes <https://github.com/doctrine/mongodb-odm/pull/1219>`__
for ``EmbedMany`` and ``ReferenceMany`` associations.

The current ``master`` branch will soon become development branch for 1.1 and the
*PHP requirement will be bumped to 5.5*. If you cannot upgrade your PHP runtime,
please continue to use the 1.0.x branch. If you are interested in testing the
latest bug fixes (before we tag them), you may want to follow the
`1.0.x branch <https://github.com/doctrine/mongodb-odm/tree/1.0.x>`__.

.. author:: Maciej Malarz <malarzm@gmail.com>
.. categories:: none
.. tags:: none
.. comments::
