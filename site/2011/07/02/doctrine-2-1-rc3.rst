Doctrine 2.1 Release Candidate 3
================================

We released Doctrine 2.1 Release Candidate 3 after some important
changes to the new annotation reader. That is also why we didnt
manage to keep our release date of June 30th. The new date is
Monday.

About the Annotations: We constantly had problems with the
autoloading of annotations through PHP autoloaders, increasing with
Symfony2 starting to use the reader with enabled autoloading. The
problem with reusing the PHP autoloader can be explained easily:
Not every Docblock Annotation has a corresponding PHP class that
can be instantiated by Doctrines AnnotationReader. The question is
how we detect the annotations from the documentation related
comments only. The solution required a silent autoloader, meaning
no failure should occur if an autoload is triggered for a
non-existant class. Implementing such an autoloader has performance
drawbacks though, which is why the Doctrine does not fail silently.
Autoloading annotations was not compatible with Doctrines own class
loader.

That problem is why we removed PHP autoloading completely and
reimplemented our own autoloading mechanism inside Doctrine
Annotations. Now we have much more control about when errors occur
and if we skip them or throw an exception.

See `this following Gist <https://gist.github.com/1059486>`_ on how
autoloading annotations works. This is not relevant if you use
$config->newDefaultAnnotationDriver() with the ORM though, which
will handle all the necessary bootstrapping for you.

Additionally we have changed the annotation reader in other
aspects. To be a valid annotation your class have to extend
(backwards compatible way, will be removed in 3.0.x) or contain
@Annotation inside the class level docblock.

We will update the documentation for Doctrine Common accordingly in
the next hours to allow you to understand all the changes made
between 2.0 and 2.1.

If you are using Annotations either in Doctrine 2 or within your
own code please update and check the changes.



.. author:: beberlei <kontakt@beberlei.de>
.. categories:: none
.. tags:: none
.. comments::
