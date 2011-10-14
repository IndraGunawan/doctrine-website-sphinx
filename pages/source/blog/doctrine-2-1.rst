:author: beberlei <kontakt@beberlei.de>
:date: 2011-07-04 18:06:00

=====================
Doctrine 2.1 released
=====================

We finished all the outstanding work on the Doctrine 2.1 branch and
released the first final version. Almost all of the code was kept
backwards compatible. There are only some slight changes that are
explained in the
`UPGRADE\_TO\_2\_1 file <https://github.com/doctrine/doctrine2/blob/master/UPGRADE_TO_2_1>`_.

This release is packed with new features and optimizations:


-  **Indexed associations:** You can force Doctrine to hydrate
   collection elements by using a field of the target entity as key,
   for example the ID or any unique field. See the
   `tutorial for this feature <http://www.doctrine-project.org/docs/orm/2.0/en/tutorials/working-with-indexed-associations.html>`_.
-  **Extra Lazy Collections:** Instead of always initializing the
   complete collection in memory you can now mark a collection as
   extra lazy, leading to special SQL executed for Collection#count(),
   Collection#contains() and Collection#slice(). This allows to
   implement efficient pagination on collections without having to use
   DQL. It also allows to save some memory for common use-cases with
   very large collections. See the
   `tutorial for this feature <http://www.doctrine-project.org/docs/orm/2.0/en/tutorials/extra-lazy-associations.html>`_.
-  **Identity through Foreign Entities or derived entities:** You
   can now use a foreign key as identifier of an entity. This
   translates to using @Id on a @ManyToOne or @OneToOne association.
   You can read up on this
   `feature in the tutorial <http://www.doctrine-project.org/docs/orm/2.0/en/tutorials/composite-primary-keys.html#identity-through-foreign-entities>`_.
-  **Persister Refactoring:** Instead of reimplementing hydration
   in the persisters we now use the hydration mechanism that is used
   by DQL aswell. Sadly this drops performance for hydration in the
   persisters by 5-25% for some use-cases. It starts with a drop of 5%
   for a few hydrations and increases in the number of different
   hydrations you are doing in a request. As a benefit we could remove
   tons of code and use several optimizations that actually increase
   performance when using fetch="EAGER" in ManyToOne and OneToOne
   associations. Furthermore inverse OneToOne associations previously
   always executed an additional query, which is now replaced with a
   join.
-  **Temporary fetch mode in DQL** On a DQL Query you can now call
   :math:`$query->setFetchMode($`className, $assocName, $fetchMode) to
   temporarily set the fetch mode to a value different from the one
   defined in the Association Mapping. If you set a ManyToOne or
   OneToOne association to eager fetching Doctrine will use a batch
   WHERE id IN (..) query to fetch all entities in a single query
   after the original query was completed.
-  **Binding Arrays to a Query:** Doctrine now implements low-level
   support for binding arrays to named or positional parameters. This
   is possible with the Doctrine::TYPE\_INT\_ARRAY and
   Doctrine::TYPE\_STR\_ARRAY parameters that you have to pass as
   types to a query you want to use this feature in. EntityRepository
   now supports passing arrays as values to a field and uses an IN
   query.
-  **EntityRepository Limit and OrderBy:** The method
   EntityRepository#findBy() now accepts additional parameters for
   ordering, limit and offset.
-  **ResultSetMapping Helper:** There is now a class that
   simplifies populating a ResultSetMapping based on an existing
   ClassMetadata instance.
-  **Zero Based Parameters in Queries:** You can now start with the
   parameter ?0 in DQL queries.
-  **Named DQL Queries in Metadata:** You can add dql queries in
   the mapping files using @NamedQueries(@NamedQuery(name="foo",
   query="DQL")) and access them through
   $em->getRepository()->getNamedQuery().
-  **Date related DQL functions:** Suport for DATE\_ADD(),
   DATE\_SUB() and DATE\_DIFF() in DQL.
-  **New console command orm:info:** Gives details about all
   registered entities and if their mappings are valid or not.
-  **Read Only Entities:** You can set the attribute readOnly=true
   on an entity. This will only allow to persist new instances of this
   entity or removing them, they will never be considered for
   updating, thus allowing for performance optimizations where these
   entities are not considered in the UnitOfWork changeset
   computations.
-  **SQL Query Object:** There is now an SQL Query object in the
   Doctrine project. You can create an instance with
   $connection->createQueryBuilder().
-  **Automatic Parameter Type Inference:** For certain parameters
   types such as integer and DateTime ORM Query::setParameter can now
   automatically infer the type instead of requiring manually passing
   the values as third parameter.
-  **AnnotationReader Refactoring** - The annotation reader is now
   much more powerful and also allows for giving you error advices if
   you configure it this way. See the
   `documentation <http://www.doctrine-project.org/docs/common/2.1/en/reference/annotations.html>`_
   on all the changes and how Annotations work in 2.1.

See the changelogs for a list of all changes:


-  `Doctrine ORM 2.1 Changelog <http://www.doctrine-project.org/jira/browse/DDC/fixforversion/10022>`_
-  `Doctrine DBAL 2.1 Changelog <http://www.doctrine-project.org/jira/browse/DBAL/fixforversion/10068>`_
-  `Doctrine Common 2.1 Changelog <http://www.doctrine-project.org/jira/browse/DCOM/fixforversion/10123>`_

You can grab the code from our
`downloads section <http://www.doctrine-project.org/projects>`_,
from `PEAR <http://pear.doctrine-project.org>`_ or directly from
`Github <http://github.com/doctrine>`_.

I will announce winners of the backwards compatibility competition
in the next weeks and send out gifts. The team thanks all
contributors and bug-reporters for helping making Doctrine 2.1 a
stable release. The next release of Doctrine 2.2 is scheduled for
December 2011. We havent quite made up our mind on the roadmap yet,
but expect a post on this issue soon.


