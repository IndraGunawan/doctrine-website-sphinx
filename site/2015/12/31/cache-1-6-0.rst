Cache 1.6.0 Released
====================

We are happy to announce the immediate availability of Doctrine Cache
`1.6.0 <https://github.com/doctrine/cache/releases/tag/v1.5.2>`_.

Cache 1.6.0
~~~~~~~~~~~

Support for PHP versions below 5.5.0 was removed: please remember that if
you are still using PHP 5.4.x or lower, the PHP project
`does not provide support for those versions anymore <http://php.net/supported-versions.php>`_. `#109 <https://github.com/doctrine/cache/pull/109>`_

Native `APCu <https://github.com/krakjoe/apcu>`_ support was introduced:
if you run newer versions of APCu, then you can use the
new `ApcuCache <https://github.com/doctrine/cache/blob/v1.6.0/lib/Doctrine/Common/Cache/ApcuCache.php>`_
adapter. `#115 <https://github.com/doctrine/cache/pull/117>`_

A `MultiPutCache <https://github.com/doctrine/cache/blob/v1.6.0/lib/Doctrine/Common/Cache/MultiPutCache.php>`_
interface was introduced: the
`CacheProvider <https://github.com/doctrine/cache/blob/v1.6.0/lib/Doctrine/Common/Cache/CacheProvider.php>`_
implements it by default now. This interface can lead to improved
performance when saving multiple keys at once, if your cache adapter
supports such an operation. `#117 <https://github.com/doctrine/cache/pull/117>`_

The `ArrayCache <https://github.com/doctrine/cache/blob/v1.6.0/lib/Doctrine/Common/Cache/ArrayCache.php>`_
now honors the given cache entries TTL, making it possible to use
it even in long running processes without the risk of dealing with
stale data. `#130 <https://github.com/doctrine/cache/pull/130>`_

Installation
~~~~~~~~~~~~

You can install the Cache component using the following ``composer.json`` definitions:

.. code-block:: shell

  composer require doctrine/cache:^1.6

Please report any issues you may have with the update on the mailing list or on
`Jira <http://www.doctrine-project.org/jira>`_.

.. author:: Marco Pivetta <ocramius@gmail.com>
.. categories:: Release
.. tags:: none
.. comments::
