Doctrine 1.0.7 is Available!
============================

Today I have made available
`Doctrine 1.0.7 <http://www.doctrine-project.org/download>`_ , the
latest bug fix release for the 1.0 version of Doctrine. This
release is a significant one with a few dozen bugs fixed. Below is
a list that highlights some of the fixes.

Highlights
~~~~~~~~~~


-  [r5361] Fixed NestedSet to not create column for root column if
   it already exists (closes #1817)
-  [r5419] Fixes #1856. Added checking to schema file to ensure
   correct file extension (format).
-  [r5429] Fixes issue with generated count queries (closes #1766)
-  [r5438] Fixes issue with saveRelated() being called too early
   (closes #1865)
-  [r5441] Fixing generated models to adhere to coding standard of
   using 4 spaces (closes #1846)
-  [r5459] Fixes issue with I18n and column aliases (closes #1824)

Lots of other fixes have been made in this release so if you want
to see a list of all the changes be sure to check the
`changelog <http://www.doctrine-project.org/change_log/1_0_7>`_.



.. author:: jwage 
.. categories:: none
.. tags:: none
.. comments::
