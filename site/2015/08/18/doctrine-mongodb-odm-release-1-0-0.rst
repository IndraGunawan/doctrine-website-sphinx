Doctrine MongoDB ODM release 1.0.0
==================================

In observance of August 18th, the day that Jon Wage tagged Doctrine MongoDB ODM's
`first BETA release <https://github.com/doctrine/mongodb-odm/releases/tag/1.0.0BETA1>`__,
we've come together for a big celebration. From humble beginnings as a weekend
hack to port Doctrine 2's data mapper pattern to NoSQL, the ODM quickly became a
beast of a project and cut its teeth on production servers early on as a core
ependency of the very first Symfony2 startups. Today, after five years of
adoption, improvements, refactoring, and
`countless jokes <https://twitter.com/jmikola/status/583047759160336384?lang=en>`__…
we are very happy to announce the immediate availability of Doctrine MongoDB ODM
1.0.0!

What is new in 1.0.0?
---------------------

For our first stable release, we focused on fixing most known bugs (some of
which were open for *years*), hardening existing features, and straightening out
ODM's behaviour and correctness where possible. In hopes of ensuring a pleasant
upgrade experience, we have prepared a
`checklist <https://github.com/doctrine/mongodb-odm/blob/master/CHANGELOG-1.0.md#100-2015-08-18>`__
for you, which highlights the most important changes that may require your
attention. A complete list of resolved issues and pull requests may be found on
GitHub under the `1.0.0 milestone <https://github.com/doctrine/mongodb-odm/issues?q=milestone%3A1.0.0>`__.

Behind the scenes: Doctrine MongoDB 1.2.0
-----------------------------------------

We are also happy to announce the immediate availability of Doctrine MongoDB
1.2.0, which is the underlying driver abstraction layer employed by the ODM.
In particular, this release sports a brand new
`Aggregation Builder <https://github.com/doctrine/mongodb/pull/213>`__, along
with improved query builder support for
`update operators <https://github.com/doctrine/mongodb/pull/212>`__ and
and `full-text search <https://github.com/doctrine/mongodb/pull/184>`__
introduced in MongoDB 2.6. For a full list of closed issues and pull requests,
please see the `release notes on GitHub <https://github.com/doctrine/mongodb/releases/tag/1.2.0>`__.

Stop fooling around, I want my BETA back!
-----------------------------------------

We apologize for any inconvenience, but Doctrine MongoDB ODM has officially gone
stable and we don't intend on shipping more BETAs anytime soon. Well, at least
not until work begins on 2.0 :D

.. author:: Maciej Malarz <malarzm@gmail.com>
.. categories:: none
.. tags:: none
.. comments::
