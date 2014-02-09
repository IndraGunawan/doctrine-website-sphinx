Security releases 2.0.8 and 2.1.2
=================================

It was brought to our attention that identifier quoting in Doctrine
DBAL has a potential security problem when user-input is passed
into this function, making the security aspect of this
functionality obsolete. We fixed as soon as we realized it and
apologize for to our users for this error.

We released versions 2.1.2 and 2.0.8 of DBAL that both contain a
fix for the problem. You can grab the code from
`PEAR <http://pear.doctrine-project.org>`_ ,
`Github <http://github.com/doctrine/dbal>`_ or the
`Downloads section <http://www.doctrine-project.org/projects/dbal/download>`_.

If you make use of AbstractPlatform::quoteIdentifier() or
Doctrine::quoteIdentifier() please upgrade immediately. The ORM
itself does not use identifier quoting in combination with
user-input, however we still urge everyone to update to the latest
version of DBAL.



.. author:: beberlei 
.. categories:: Release
.. tags:: none
.. comments::
