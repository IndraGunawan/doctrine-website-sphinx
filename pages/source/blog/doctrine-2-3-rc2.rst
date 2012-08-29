:author: beberlei <kontakt@beberlei.de>
:date: 2012-08-29 10:06:00

===========================
Doctrine 2.3.0 RC2 released
===========================

**29.8.2012**

We released another release candidate of our upcoming
Doctrine 2.3.0 version. This includes the Common, DBAL
and ORM packages.

This release trys to keep backwards compatibility to every previous release as
much as possible, however some slight changes might be necessary to your
applications. See the UPGRADE files of each project for details:

* `ORM <https://github.com/doctrine/doctrine2/blob/master/UPGRADE.md>`_
* `DBAL <https://github.com/doctrine/dbal/blob/master/UPGRADE>`_

See the `2.3 Beta blog post
<http://www.doctrine-project.org/blog/doctrine-2-3-beta.html>`_ for some
information about changes in 2.3.

You can install the release candidate through `Github <https://github.com/doctrine/doctrine2>`_  or `Composer <http://www.packagist.org>`_:

.. code-block:: 

    {
        "require": {
            "doctrine/orm": "2.3.0-RC2"
        },
        "minimum-stability": "dev"
    }

If you find any problems with your applications please report them on our
`bugtracker <http://www.doctrine-project.org/jira>`_.

When no blocking issues occur we will release the 2.3.0 final
on next Monday.
