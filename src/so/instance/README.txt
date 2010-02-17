======================================
 Superorganism Buildout Instance Recipe
======================================

This buildout recipe creates an instance to run superorganism
bugtracker.

The instance recipe has several options:

script
    The script option gives the name of the script to be generated in
    the bin buildout directory. By default, the name of the part is
    used.

database
    A path where the Data.fs will be created. By default
    ${buildout:directory}/var/Data.fs will be used.

We start with a minimal buildout recipe:

>>> write(sample_buildout, 'buildout.cfg', 
... """
... [buildout]
... parts = superorganism
...
... [superorganism]
... recipe = so.recipe.instance
... database = %s/Data.fs
... """ % sample_buildout)

