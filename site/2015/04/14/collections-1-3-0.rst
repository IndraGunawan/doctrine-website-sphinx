Doctrine Collections 1.3.0 Release
==================================

We are happy to announce the immediate availability of Doctrine Collections ``1.3.0``.

Installation
------------

You can install this version of Doctrine Common by using Composer and the
following ``composer.json`` contents:

.. code-block:: json

  {
      "require": {
          "doctrine/collections": "1.3.0"
      }
  }

Changes since 1.3.0
-------------------

This is a list of issues solved in ``1.3.0`` since ``1.2.0``:

- `[26] <https://github.com/doctrine/collections/pull/26>`_: Explicit casting of first and max results in the criteria API
- `[30] <https://github.com/doctrine/collections/pull/30>`_: typo fixes
- `[31] <https://github.com/doctrine/collections/pull/31>`_: CS fixes and tidy up of the tests
- `[36] <https://github.com/doctrine/collections/pull/36>`_: Tidy up and CS fixes
- `[42] <https://github.com/doctrine/collections/pull/42>`_: small style changes to comply with PSR2
- `[47] <https://github.com/doctrine/collections/pull/47>`_: Added build status badge
- `[49] <https://github.com/doctrine/collections/pull/49>`_: Keep keys when using ``ArrayCollection#matching()``
- `[52] <https://github.com/doctrine/collections/pull/52>`_: Made ``AbstractLazyCollection#$initialized`` protected for extensibility.
- `[56] <https://github.com/doctrine/collections/pull/56>`_: travis: PHP 7.0 nightly added + few improvements

Please report any issues you may have with the update on the mailing list or on
`Jira <http://www.doctrine-project.org/jira/browse/DCOM>`_.

.. author:: Marco Pivetta <ocramius@gmail.com>
.. categories:: none
.. tags:: none
.. comments::
