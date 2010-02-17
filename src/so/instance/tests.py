from unittest import TestSuite
from doctest import COMPARISON_FLAGS, REPORT_ONLY_FIRST_FAILURE
from zope.testing import doctestunit
from zc.buildout.testing import buildoutSetUp, install_develop


def setUp(test):
    buildoutSetUp(test)
    install_develop('zope.interface', test)
    install_develop('zope.testing', test)
    install_develop('Cheetah', test)
    install_develop('iw.recipe.template', test)
    install_develop('so.instance', test)

def test_suite():
    """ returns the test suite """
    return TestSuite([
        doctestunit.DocFileSuite(
           'README.txt', package='so.instance',
           optionflags=COMPARISON_FLAGS | REPORT_ONLY_FIRST_FAILURE, setUp=setUp)
    ])
