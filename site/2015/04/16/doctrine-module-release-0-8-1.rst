Doctrine Module release 0.8.1
=============================

The **Zend Framework Integration Team** is happy to announce the new release of **DoctrineModule**.
DoctrineModule ``0.8.1`` will be the last bugfix, it is the last version that will support PHP 5.3.
Further versions of the ``0.8.*`` series may still be released in case of security issues.

Following issues were solved in this release:
 - `[#376] Bumping PHP and ZF2 dependencies, branch alias for master <https://github.com/doctrine/DoctrineModule/pull/376>`_
 - `[#378] I think this is a small PSR rule violation. <https://github.com/doctrine/DoctrineModule/pull/378>`_
 - `[#381] Update validator.md <https://github.com/doctrine/DoctrineModule/pull/381>`_
 - `[#388] Added exception for missing required parameter for find_method option as <https://github.com/doctrine/DoctrineModule/pull/388>`_
 - `[#390] Clarified how to pass sort information. <https://github.com/doctrine/DoctrineModule/pull/390>`_
 - `[#395] Issue with objects being cast to array in validators <https://github.com/doctrine/DoctrineModule/pull/395>`_
 - `[#397] Enhancement: use exit code from run() <https://github.com/doctrine/DoctrineModule/pull/397>`_
 - `[#401] Reading Inconsistency <https://github.com/doctrine/DoctrineModule/pull/401>`_
 - `[#391] UniqueObject Validator * allowing composite identifiers from context or not <https://github.com/doctrine/DoctrineModule/pull/391>`_
 - `[#400] let zf2 console return exit status <https://github.com/doctrine/DoctrineModule/pull/400>`_
 - `[#404] Fix form elements <https://github.com/doctrine/DoctrineModule/pull/404>`_
 - `[#406] Fix context unique <https://github.com/doctrine/DoctrineModule/pull/406>`_
 - `[#421] Make DoctrineObject use AbstractHydrator s namingStrategy <https://github.com/doctrine/DoctrineModule/pull/421>`_
 - `[#426] update year in license <https://github.com/doctrine/DoctrineModule/pull/426>`_
 - `[#436] Fixing typo and updating paginator link to ZF 2.3 <https://github.com/doctrine/DoctrineModule/pull/436>`_
 - `[#450] minor cs fix <https://github.com/doctrine/DoctrineModule/pull/450>`_
 - `[#458] Update doctrine*module.php <https://github.com/doctrine/DoctrineModule/pull/458>`_
 - `[#462] Adding custom Doctrine*Cli Commands <https://github.com/doctrine/DoctrineModule/pull/462>`_
 - `[#465] Re*enable scrutinizer*ci code coverage <https://github.com/doctrine/DoctrineModule/pull/465>`_
 - `[#453] phpdoc fixes <https://github.com/doctrine/DoctrineModule/pull/453>`_

To install this version, simply update your `composer.json`:

.. code-block:: json

  {
      "require": {
          "doctrine/doctrine-module": "0.8.1"
      }
  }

.. author:: Gianluca Arbezzano <gianarb92@gmail.com>
.. categories:: none
.. tags:: none
.. comments::
