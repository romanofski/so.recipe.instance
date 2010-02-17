from setuptools import setup, find_packages

name = "so.instance"
setup(
    name = name,
    version = "0.1",
    author = "Roman Joost",
    author_email = "roman@bromeco.de",
    description = "zc.buildout recipe to run a superorganism instance.",
    long_description = open('README.txt').read() + 
        '\n\n' + 
        open('CHANGES.txt').read(),
    license = "GPL",
    keywords = "buildout recipe superorganism bugtracker",
    classifiers = ["Framework :: Buildout"],
    zip_safe=False,
    packages = find_packages('src'),
    include_package_data = True,
    package_dir = {'':'src'},
    namespace_packages = ['so'],
    entry_points = {
        'zc.buildout': [
             'default = %s:Recipe' % name],
        'zc.buildout.uninstall': [
            'default = %s:uninstall' % name],
        },
    test_suite = 'so.instance.tests.test_recipe.test_suite',
    tests_require = ['zope.testing',
                     'iw.recipe.template',
                    ],
    install_requires = ['zc.buildout',
                        'setuptools',
                        'iw.recipe.template',
                       ],
    )
