# -*- coding: utf-8 -*-

import unittest2 as unittest

from zope.component import createObject
from zope.component import queryUtility

from Products.CMFCore.utils import getToolByName
from plone.app.testing import TEST_USER_ID
from plone.app.testing import setRoles
from plone.dexterity.interfaces import IDexterityFTI

from sg.questions.testing import INTEGRATION_TESTING
from sg.questions.question import IQuestion


class TestquestionsIntegration(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.portal.invokeFactory('Folder', 'test-folder')
        setRoles(self.portal, TEST_USER_ID, ['Member'])
        self.folder = self.portal['test-folder']

    def test_adding(self):
        self.folder.invokeFactory('sg.questions.question', 'question1')
        question1 = self.folder['question1']
        self.failUnless(IQuestion.providedBy(question1))

    def test_fti(self):
        fti = queryUtility(IDexterityFTI, name='sg.questions.question')
        self.assertNotEquals(None, fti)

    def test_schema(self):
        fti = queryUtility(IDexterityFTI, name='sg.questions.question')
        schema = fti.lookupSchema()
        self.assertEquals(IQuestion, schema)

    def test_factory(self):
        fti = queryUtility(IDexterityFTI, name='sg.questions.question')
        factory = fti.factory
        new_object = createObject(factory)
        self.failUnless(IQuestion.providedBy(new_object))


def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
