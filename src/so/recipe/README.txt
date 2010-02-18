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
scripttemplate
    A python template which generates the rest of the instance script.

We start with a minimal buildout recipe:

>>> write(sample_buildout, 'buildout.cfg', 
... """
... [buildout]
... parts = superorganism
...
... [superorganism]
... recipe = so.recipe""")

Script Template
===============

The recipe should create a script to run the superorganism bugtracker:

>>> print system(buildout)
superorganism: Cannot find ...
Error: Invalid Path to script template

We forgot to configure the script template. It is used to import and
initialize the application, register basic utilities (like the
Database). We could have hardcoded it into the recipe. This provides
more flexibility for the developer to initialize the instance.

>>> write(sample_buildout, 'script.tmpl',
... """
... import superorganism.app
... superorganism.app.App(%s)
... """ % sample_buildout)

This is obviously not a correct template to run the application, but is
used to illustrate the generation of the instance python script:

>>> write(sample_buildout, 'buildout.cfg', 
... """
... [buildout]
... parts = superorganism
...
... [superorganism]
... recipe = so.recipe
... scripttemplate = %s/script.tmpl
... """ % sample_buildout)
>>> print system(buildout)
Installing superorganism.
... Generated script '...bin/superorganism'...

The superorganism script should now have also our template included:

>>> ls('bin')
- buildout
- superorganism
>>> cat('bin/superorganism')
#!...
import sys
sys.path...
import superorganism.app
superorganism.app.App(...)

If we use a different name for the script name, our generated script
will have obviously a different name:

>>> write(sample_buildout, 'buildout.cfg', 
... """
... [buildout]
... parts = superorganism
...
... [superorganism]
... recipe = so.recipe
... script = instance
... database = %s/Data.fs
... """ % sample_buildout)
>>> print system(buildout)
Uninstalling superorganism.
Installing superorganism.
... Generated script '...bin/instance'...
