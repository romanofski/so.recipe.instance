import os.path
from setuptools import setup, find_packages


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()


name = "so.recipe.instance"
setup(
    name = name,
    version = "0.1",
    author = "Roman Joost",
    author_email = "roman@bromeco.de",
    description = "zc.buildout recipe to run a superorganism instance.",
    long_description = read('README.txt') +
        '\n\n' +
        read('so', 'recipe', 'instance', 'README.txt') +
        '\n\n' +
        read('CHANGES.txt'),
    license = "GPL",
    keywords = "buildout recipe superorganism bugtracker",
    classifiers = ["Framework :: Buildout"],
    zip_safe=False,
    packages = find_packages(exclude=['ez_setup']),
    namespace_packages = ['so', 'so.recipe'],
    include_package_data = True,
    entry_points = {
        'zc.buildout': [
             'default = %s:Recipe' % name],
        'zc.buildout.uninstall': [
            'default = %s:uninstall' % name],
        },
    test_suite = 'so.recipe.instance.tests.test_recipe.test_suite',
    tests_require = ['zope.testing',
                     'iw.recipe.template',
                    ],
    install_requires = ['zc.buildout',
                        'setuptools',
                        'iw.recipe.template',
                        'zc.recipe.egg',
                       ],
    )
