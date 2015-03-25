Doctrine ORM 2.5.0-RC1 Release Candidate
========================================

We are happy to announce the immediate availability of Doctrine ORM ``2.5.0-RC1``.

This is a release candidate meant to allow users and contributors to verify the
stability of the next iteration of the ORM.

We encourage all of our users to help us by trying out this release.
Please report any possible problems or incompatibilities that may have been
introduced during development.

What is new in 2.5.x?
~~~~~~~~~~~~~~~~~~~~~

We are currently in the process of documenting all the changes and new features that were
introduced in Doctrine ORM 2.5.x.

You can find the current state of the 2.5.0 changes overview in
`the upgrade notes <http://docs.doctrine-project.org/en/latest/changelog/migration_2_5.html>`_.

Release RoadMap
~~~~~~~~~~~~~~~

We expect to release following versions of the ORM in the next days:

 - ``2.5.0`` on ``2015-04-02``

Please note that these dates may change depending on the availability of our team.

We also apologise for the major delays in this beta release, which are caused by
the scarce availability of the core team in these months.

Installation
~~~~~~~~~~~~

You can install this version of the ORM by using Composer and the
following ``composer.json`` contents:

.. code-block:: json

  {
      "require": {
          "doctrine/orm": "2.5.0-RC1"
      },
      "minimum-stability": "dev"
  }
```

Changes since 2.5.0-beta2
~~~~~~~~~~~~~~~~~~~~~~~~~

This is a list of issues solved in ``2.5.0-RC1`` since ``2.5.0-beta1``:

- [`DDC-3632 <http://www.doctrine-project.org/jira/browse/DDC-3632>`_]
  [`#1345 <https://github.com/doctrine/doctrine2/pull/1345>`_] Fix crashes in ``ConvertMappingCommand`` and
  ``GenerateEntitiesCommand`` when using entities with joined table inheritance
- [`DDC-3634 <http://www.doctrine-project.org/jira/browse/DDC-3634>`_]
  [`#1346 <https://github.com/doctrine/doctrine2/pull/1346>`_] Fix: generated IDs are converted to integer even
  when they are big integers
- [`DDC-3630 <http://www.doctrine-project.org/jira/browse/DDC-3630>`_]
  [`DDC-3621 <http://www.doctrine-project.org/jira/browse/DDC-3621>`_]
  [`#1343 <https://github.com/doctrine/doctrine2/pull/1343>`_] Support embeddables in partial object query expression
- [`DDC-3623 <http://www.doctrine-project.org/jira/browse/DDC-3623>`_]
  [`DDC-3629 <http://www.doctrine-project.org/jira/browse/DDC-3629>`_]
  [`#1337 <https://github.com/doctrine/doctrine2/pull/1337>`_]
  [`#1342 <https://github.com/doctrine/doctrine2/pull/1342>`_] Paginator functional tests and sorting corrections
- [`DDC-2224 <http://www.doctrine-project.org/jira/browse/DDC-2224>`_]
  [`DDC-3625 <http://www.doctrine-project.org/jira/browse/DDC-3625>`_]
  [`#1339 <https://github.com/doctrine/doctrine2/pull/1339>`_] Honor ``convertToDatabaseValueSQ`` in DQL query
  parameters and caches

Please report any issues you may have with the update on the mailing list or on
`Jira <http://www.doctrine-project.org/jira/browse/DDC>`_.

.. author:: Marco Pivetta <ocramius@gmail.com>
.. categories:: none
.. tags:: none
.. comments::
