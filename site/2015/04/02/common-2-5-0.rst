Doctrine Common 2.5.0 Release
=============================

We are happy to announce the immediate availability of Doctrine Common `2.5.0`.

Installation
------------

You can install this version of Doctrine Common by using Composer and the
following ``composer.json`` contents:

.. code-block:: json

  {
      "require": {
          "doctrine/common": "2.5.0"
      }
  }

Changes since 2.4.x
-------------------

This is a list of issues solved in ``2.5.0`` since ``2.4.x``:

Bug
~~~

- [`DCOM-129 <http://www.doctrine-project.org/jira/browse/DCOM-129>`_] - Annotation parser matches colon after annotation
- [`DCOM-151 <http://www.doctrine-project.org/jira/browse/DCOM-151>`_] - [`GH-233 <https://github.com/doctrine/common/pull/233>`_] [DocParser] Fix trying include classes if its must be ignored.
- [`DCOM-162 <http://www.doctrine-project.org/jira/browse/DCOM-162>`_] - [`GH-244 <https://github.com/doctrine/common/pull/244>`_] return parameter for debug method
- [`DCOM-168 <http://www.doctrine-project.org/jira/browse/DCOM-168>`_] - ignoredAnnotationNames doesn't work in Annotation loop
- [`DCOM-175 <http://www.doctrine-project.org/jira/browse/DCOM-175>`_] - Proxies return private properties in __sleep, which is not supported by PHP.
- [`DCOM-191 <http://www.doctrine-project.org/jira/browse/DCOM-191>`_] - Wrong inflection for "identity"
- [`DCOM-212 <http://www.doctrine-project.org/jira/browse/DCOM-212>`_] - [`GH-296 <https://github.com/doctrine/common/pull/296>`_] Proxies shouldn't serialize static properties in __sleep()
- [`DCOM-216 <http://www.doctrine-project.org/jira/browse/DCOM-216>`_] - [`GH-298 <https://github.com/doctrine/common/pull/298>`_] Silence E_NOTICE warning: "Undefined index".
- [`DCOM-220 <http://www.doctrine-project.org/jira/browse/DCOM-220>`_] - [`GH-304 <https://github.com/doctrine/common/pull/304>`_] fix typo
- [`DCOM-223 <http://www.doctrine-project.org/jira/browse/DCOM-223>`_] - [`GH-308 <https://github.com/doctrine/common/pull/308>`_] fix the optimize regex and adapt the tests to actually test classAnnotat...
- [`DCOM-228 <http://www.doctrine-project.org/jira/browse/DCOM-228>`_] - [`GH-312 <https://github.com/doctrine/common/pull/312>`_] Improve UnexpectedValueException error message
- [`DCOM-261 <http://www.doctrine-project.org/jira/browse/DCOM-261>`_] - [`GH-344 <https://github.com/doctrine/common/pull/344>`_] Fix fatal error when classexist tries to call the protected loader
- [`DCOM-270 <http://www.doctrine-project.org/jira/browse/DCOM-270>`_] - [`GH-351 <https://github.com/doctrine/common/pull/351>`_] Added validation where allowed QCNs with ":" NS separator
- [`DCOM-272 <http://www.doctrine-project.org/jira/browse/DCOM-272>`_] - Proxy generator doesn't understand splat operator (PHP 5.6 argument unpacking)

Documentation
~~~~~~~~~~~~~

- [`DCOM-237 <http://www.doctrine-project.org/jira/browse/DCOM-237>`_] - [`GH-318 <https://github.com/doctrine/common/pull/318>`_] Fixed link to Documentation
- [`DCOM-280 <http://www.doctrine-project.org/jira/browse/DCOM-280>`_] - [`GH-359 <https://github.com/doctrine/common/pull/359>`_] Fixed missing / incorrect docblocks

Improvement
~~~~~~~~~~~

- [`DCOM-246 <http://www.doctrine-project.org/jira/browse/DCOM-246>`_] - [`GH-328 <https://github.com/doctrine/common/pull/328>`_] Optimized imports
- [`DCOM-247 <http://www.doctrine-project.org/jira/browse/DCOM-247>`_] - [`GH-329 <https://github.com/doctrine/common/pull/329>`_] Remove dead config
- [`DCOM-263 <http://www.doctrine-project.org/jira/browse/DCOM-263>`_] - [`GH-347 <https://github.com/doctrine/common/pull/347>`_] Class loader: skip non-existing files and files not containing the requested class
- [`DCOM-278 <http://www.doctrine-project.org/jira/browse/DCOM-278>`_] - [`GH-358 <https://github.com/doctrine/common/pull/358>`_] travis: PHP 7.0 nightly added, allowed failure

New Feature
~~~~~~~~~~~

- [`DCOM-257 <http://www.doctrine-project.org/jira/browse/DCOM-257>`_] - [`GH-342 <https://github.com/doctrine/common/pull/342>`_] Class metadata loading fallback hook in AbstractClassMetadataFactory
- [`DCOM-277 <http://www.doctrine-project.org/jira/browse/DCOM-277>`_] - [`GH-357 <https://github.com/doctrine/common/pull/357>`_] Custom namespace separators for SymfonyFileLocator

Please report any issues you may have with the update on the mailing list or on
`Jira <http://www.doctrine-project.org/jira/browse/DCOM>`_.
