Inflector 1.0.1 released
========================

We are happy to announce the immediate availability of ``doctrine/inflector`` 1.0.1.

The release includes minor fixes since the first 1.0.0 release, and also stabilizes
and enforces support for HHVM.

- `49: #46 - applying correct chmod() to generated cache file <https://github.com/doctrine/annotations/pull/49>`_
- `50: Hotfix: match escaped quotes (revert #44) <https://github.com/doctrine/annotations/pull/50>`_

- `1: Corrected keyword spelling <https://github.com/doctrine/inflector/pull/1>`_
- `2: Documentation fixes <https://github.com/doctrine/inflector/pull/2>`_
- `3: Added the branch alias for master <https://github.com/doctrine/inflector/pull/3>`_
- `4: Fixed typo <https://github.com/doctrine/inflector/pull/4>`_
- `5: exclude word 'staff' from inflectable ones <https://github.com/doctrine/inflector/pull/5>`_
- `6: add LICENSE file <https://github.com/doctrine/inflector/pull/6>`_
- `7: HHVM is not allowed to fail anymore. Inflector should work as expected <https://github.com/doctrine/inflector/pull/7>`_
- `10: Added the local phpunit config to the ignore list <https://github.com/doctrine/inflector/pull/10>`_
- `12: Adding 'human' to the irregular array <https://github.com/doctrine/inflector/pull/12>`_
- `14: Add testing on PHP 5.6 on Travis <https://github.com/doctrine/inflector/pull/14>`_


You can install the Inflector library using Composer and the following ``composer.json``
contents:

.. code-block:: json

  {
      "require": {
          "doctrine/inflector": "1.0.1"
      }
  }

.. author:: Marco Pivetta <ocramius@gmail.com>
.. categories:: none
.. tags:: none
.. comments::
