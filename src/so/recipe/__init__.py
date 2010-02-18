import logging
import os
import zc.buildout
import zc.recipe.egg

class Recipe(object):

    def __init__(self, buildout, name, options):
        self.buildout = buildout
        self.options = options
        self.name = name
        self.egg = zc.recipe.egg.Egg(buildout, options['recipe'], options)
        options['script'] = os.path.join(
            buildout['buildout']['bin-directory'],
            options.get('script', self.name))
        options['database'] = os.path.join(
            buildout['buildout']['directory'],
            options.get('database', 'Data.fs'))
        options['location'] = os.path.join(
            buildout['buildout']['parts-directory'],
            self.name,
        )
        if not os.path.isdir(os.path.dirname(options['database'])):
            logging.getLogger(self.name).error(
                'Cannot find database at %s.',
                options['database'], os.path.dirname(options['database']))
            raise zc.buildout.UserError('Invalid Path to Database')

    def install(self):
        dest = []
        eggs, ws = self.egg.working_set()
        ws_locations = [d.location for d in ws]
        scriptname = self.options['script']

        logging.getLogger(self.name).info(
            'Creating script %s', scriptname)
        return scriptname

    def update(self):
        pass
