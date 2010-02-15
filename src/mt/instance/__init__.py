import logging
import os
import zc.buildout

class Instance(object):

    def __init__(self, buildout, name, options):
        self.name, self.options = name, options
        options['database'] = os.path.join(
            buildout['buildout']['directory'],
            options['database'],
        )
        if not os.path.isdir(os.path.dirname(options['path'])):
            logging.getLogger(self.name).error(
                'Cannot find database at %s.',
                options['database'], os.path.dirname(options['database']))
            raise zc.buildout.UserError('Invalid Path to Database')

    def install(self):
        path = self.options['database']
        logging.getLogger(self.name).info(
            'Creating directory %s', os.path.basename(path))
        return database

    def update(self):
        pass
