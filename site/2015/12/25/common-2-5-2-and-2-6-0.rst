Common 2.5.3 and 2.6.1 Released
===============================

We are happy to announce the immediate availability of Doctrine Common
`2.5.3 <https://github.com/doctrine/common/releases/tag/v2.5.3>`_ and
`2.6.1 <https://github.com/doctrine/common/releases/tag/v2.6.1>`_.

Common 2.5.3
~~~~~~~~~~~~

This release corrects an issue with the precedence of namespaces being
matched by the ``SymfonyFileLocator```#367 <https://github.com/doctrine/common/pull/367>`_.

Common 2.6.1
~~~~~~~~~~~~

This release includes all of the fixes reported above for 2.5.3.

Installation
~~~~~~~~~~~~

You can install the Common component using Composer and one of the following
``composer.json`` definitions:

.. code-block:: json

  {
      "require": {
          "doctrine/common": "~2.5.3"
      }
  }

.. code-block:: json

  {
      "require": {
          "doctrine/common": "~2.6.1"
      }
  }

Please report any issues you may have with the update on the
`issue tracker <https://github.com/doctrine/common/issues>`_.

.. author:: Marco Pivetta <ocramius@gmail.com>
.. categories:: Release
.. tags:: none
.. comments::
