Doctrine ORM 2.5.0-alpha2 Pre-Release
=====================================

We are happy to announce the immediate availability Doctrine ORM ``2.5.0-alpha2``.

This is a pre-release meant to allow users and contributors to try out the new
upcoming features of the ORM.

We encourage all of our users to help us by trying out this alpha release.
Please report any possible problems or incompatibilities that may have been
introduced during development.

This pre-release is not yet at feature-freeze, therefore we urge contributors to contact
us if there is any change that requires our attention before we reach the beta (feature-free)
release stage.

What is new in 2.5.x?
~~~~~~~~~~~~~~~~~~~~~

We are currently in the process of documenting all the changes and new features that were
introduced in Doctrine ORM 2.5.x.

You can find the current state of the 2.5.0 changes overview in
`the upgrade notes <http://docs.doctrine-project.org/en/latest/changelog/migration_2_5.html>`_.

Release RoadMap
~~~~~~~~~~~~~~~

We expect to release following versions of the ORM in the next days:

 - ``2.5.0-beta1`` on ``2014-02-02``
 - ``2.5.0-beta2`` on ``2014-02-09``
 - ``2.5.0`` on ``2014-02-16``

Please note that these dates may change depending on the availability of our team.

Additionally, we will delay the release if any newly introduced critical bugs are
detected, as it already happened with this ``2.5.0-alpha2`` release.

Installation
~~~~~~~~~~~~

You can install this version of the ORM by using Composer and the
following ``composer.json`` contents:

.. code-block:: json

  {
      "require": {
          "doctrine/orm": "2.5.0-alpha2"
      },
      "minimum-stability": "dev"
  }

Changes since 2.5.0-alpha1
~~~~~~~~~~~~~~~~~~~~~~~~~~

This is a list of issues solved in ``2.5.0-alpha2`` since ``2.5.0-alpha1``:

 - `[DDC-3517] <http://www.doctrine-project.org/jira/browse/DDC-3517>`_
   `[GH-1265] <https://github.com/doctrine/doctrine2/pull/1265>`_ Fix error undefined
   index "targetEntity"
 - `[DDC-3516] <http://www.doctrine-project.org/jira/browse/DDC-3516>`_
   `[GH-1264] <https://github.com/doctrine/doctrine2/pull/1264>`_ Add Changelog/Migration
   to 2.5 documentation chapter.
 - `[DDC-3520] <http://www.doctrine-project.org/jira/browse/DDC-3520>`_
   `[DDC-3521] <http://www.doctrine-project.org/jira/browse/DDC-3521>`_
   `[GH-1269] <https://github.com/doctrine/doctrine2/pull/1269>`_ ``self-update`` composer
   before install
 - `[DDC-3526] <http://www.doctrine-project.org/jira/browse/DDC-3526>`_
   `[GH-1273] <https://github.com/doctrine/doctrine2/pull/1273>`_ Incorrect ``@throws``
   doc. in ``getSingleScalarResult``
 - `[DDC-3465] <http://www.doctrine-project.org/jira/browse/DDC-3465>`_
   `[GH-1232] <https://github.com/doctrine/doctrine2/pull/1232>`_ Explicit example of
   partial indexes
 - `[DDC-3300] <http://www.doctrine-project.org/jira/browse/DDC-3300>`_
   `[DDC-3503] <http://www.doctrine-project.org/jira/browse/DDC-3503>`_
   `[GH-1130] <https://github.com/doctrine/doctrine2/pull/1130>`_
   `[GH-1232] <https://github.com/doctrine/doctrine2/pull/1232>`_ Resolve target entity
   also in discriminator map (allows interfaces and custom names in discriminator map)
 - `[DDC-3378] <http://www.doctrine-project.org/jira/browse/DDC-3378>`_
   `[GH-1176] <https://github.com/doctrine/doctrine2/pull/1176>`_ Support merging entities
   with composite identities defined through to-one associations
 - `[DDC-3533] <http://www.doctrine-project.org/jira/browse/DDC-3533>`_
   `[GH-1279] <https://github.com/doctrine/doctrine2/pull/1279>`_ Fixed typos and grammar
   in the second level cache documentation
 - `[DDC-3343] <http://www.doctrine-project.org/jira/browse/DDC-3343>`_
   `[DDC-3536] <http://www.doctrine-project.org/jira/browse/DDC-3536>`_
   `[DDC-3544] <http://www.doctrine-project.org/jira/browse/DDC-3544>`_
   `[GH-1281] <https://github.com/doctrine/doctrine2/pull/1281>`_
   `[GH-1288] <https://github.com/doctrine/doctrine2/pull/1288>`_
   `[GH-1169] <https://github.com/doctrine/doctrine2/pull/1169>`_ Entities should not be
   deleted when using ``EXTRA_LAZY`` and ``one-to-many``
 - `[DDC-3538] <http://www.doctrine-project.org/jira/browse/DDC-3538>`_
   `[DDC-3519] <http://www.doctrine-project.org/jira/browse/DDC-3519>`_
   `[GH-1283] <https://github.com/doctrine/doctrine2/pull/1283>`_
   `[GH-1267] <https://github.com/doctrine/doctrine2/pull/1267>`_ Reverted
   `#1220 <https://github.com/doctrine/doctrine2/pull/1220>`_, fixed order in
   pagination logic
 - `[DDC-2704] <http://www.doctrine-project.org/jira/browse/DDC-2704>`_
   `[DDC-3524] <http://www.doctrine-project.org/jira/browse/DDC-3524>`_
   `[GH-1272] <https://github.com/doctrine/doctrine2/pull/1272>`_ merge inherited transient
   properties - merge properties into uninitialized proxies
 - `[DDC-3346] <http://www.doctrine-project.org/jira/browse/DDC-3346>`_
   `[DDC-3531] <http://www.doctrine-project.org/jira/browse/DDC-3531>`_
   `[DDC-3534] <http://www.doctrine-project.org/jira/browse/DDC-3534>`_
   `[GH-1280] <https://github.com/doctrine/doctrine2/pull/1280>`_
   `[GH-1277] <https://github.com/doctrine/doctrine2/pull/1277>`_ fixed ``findOne*``
   operations when using a ``EAGER`` ``*-to-many`` association
 - `[DDC-3541] <http://www.doctrine-project.org/jira/browse/DDC-3541>`_
   `[GH-1286] <https://github.com/doctrine/doctrine2/pull/1286>`_ Removing XDebug from
    non-coverage builds
 - `[DDC-3546] <http://www.doctrine-project.org/jira/browse/DDC-3546>`_
   `[GH-1289] <https://github.com/doctrine/doctrine2/pull/1289>`_ Improve test suite performance

Please report any issues you may have with the update on the mailing list or on
`Jira <http://www.doctrine-project.org/jira/browse/DDC>`_.

.. author:: Marco Pivetta <ocramius@gmail.com>
.. categories:: none
.. tags:: none
.. comments::
