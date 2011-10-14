:author: beberlei <kontakt@beberlei.de>
:date: 2011-06-18 18:00:00

================================
Doctrine 2.1 Release Candidate 1
================================

Doctrine 2.1 is feature complete and we packaged up the first
release candidate to celebrate this day. So far we got exactly one
backwards compability complaint that was immediately fixed. You
only have about 10 days to verify that this release candidate is
working with your existing 2.0 code-bases. If you find some
problems please report a bug on
`Jira <http://www.doctrine-project.org>`_. We will provide everyone
with mugs/tshirts who is finding incompatible changes.

We plan to release only 1-2 bugfix releases of the 2.0.x branch,
which should give you lots of motivation to try out 2.1 with your
projects.

We integrated a pretty substantial Annotation Reader refactoring
just today. Please test if this still works with your code-base
using annotations. See the
`UPGRADE\_TO\_2\_1 file <https://github.com/doctrine/doctrine2/blob/master/UPGRADE_TO_2_1>`_
for some information. You might need to adjust your bootstrapping
code to get it working.

The task now until the final release on june 30th will be to update
the documentation with all the changes that have landed in Doctrine
2.1. We already created a 2.0.x branch of the docs that will freeze
the current state for those staying on 2.0. Additionally we will
squash all the last bugs that we find.

Grab the new code in the downloads section or on our
`PEAR channel <http://pear.doctrine-project.org>`_


