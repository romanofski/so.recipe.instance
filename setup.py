from setuptools import setup, find_packages

name = "mt.instance"
setup(
    name = name,
    version = "0.1",
    author = "Róman Joost",
    author_email = "roman@bromeco.de",
    description = "zc.buildout recipe to run a metatracker instance.",
    long_description = open('README.txt').read() + 
        '\n\n' + 
        open('CHANGES.txt').read(),
    license = "GPL",
    keywords = "buildout recipe metatracker",
    classifiers = ["Framework :: Buildout"],
    zip_safe=False,
    packages = find_packages('src'),
    include_package_data = True,
    package_dir = {'':'src'},
    namespace_packages = ['mt'],
    entry_points = {
        'zc.buildout': [
             'default = %s:Recipe' % name],
        'zc.buildout.uninstall': [
            'default = %s:uninstall' % name],
        },
    test_suite = 'mt.instance.tests.test_recipe.test_suite',
    tests_require = ['zope.testing',
                     'iw.recipe.template',
                    ],
    install_requires = ['zc.buildout',
                        'setuptools',
                        'iw.recipe.template',
                       ],
    )
