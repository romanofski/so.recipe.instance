import logging
import os
import zc.buildout
import zc.recipe.egg
import iw.recipe.template
import Cheetah.Template

class Recipe(object):

    def __init__(self, buildout, name, options):
        self.buildout = buildout
        self.options = options
        self.name = name
        self.egg = zc.recipe.egg.Egg(buildout, options['recipe'], options)
        options['script'] = os.path.join(
            buildout['buildout']['bin-directory'],
            options.get('script', self.name))
        options['scripttemplate'] = os.path.join(
            buildout['buildout']['directory'],
            options.get('scripttemplate', 'script.tmpl'),
        )

        if not os.path.exists(options['scripttemplate']):
            logging.getLogger(self.name).error(
                'Cannot find %s',
                options['scripttemplate'],)
            raise zc.buildout.UserError('Invalid Path to script template')

    def install(self):
        dest = []
        eggs, ws = self.egg.working_set()
        ws_locations = [d.location for d in ws]
        scriptname = self.options['script']
        scripttempl = Cheetah.Template.Template(
            source=open(self.options['scripttemplate']).read(),
            searchList=[self.name, self.options, self.buildout]
        )
        kwargs = dict(
            source='%s/instance.tmpl' % os.path.dirname(__file__),
            destination=self.buildout['buildout']['bin-directory'],
            eggs=ws_locations,
            scripttemplate=scripttempl,
        )
        iw.recipe.template.Script(self.buildout,
                                  self.options['script'],
                                  kwargs).install()

        return scriptname

    def update(self):
        self.uninstall()
        self.install()

    def uninstall(self):
        logging.getLogger(self.name).info(
            'Removing script %s', self.options['script'])
        if os.path.exists(self.options['script']):
            os.remove(self.options['script'])
