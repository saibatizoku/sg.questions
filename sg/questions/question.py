from five import grok
from zope import schema

from Products.CMFCore.interfaces import IContentish
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.globals.interfaces import IViewView
from plone.app.layout.viewlets.interfaces import IBelowContent
from plone.app.discussion.interfaces import IDiscussionLayer
from plone.app.discussion.browser.comments import CommentsViewlet

from zope.interface import alsoProvides
from zope.publisher.interfaces.browser import IDefaultBrowserLayer

from plone.directives import form, dexterity
from plone.app.textfield import RichText
from cioppino.twothumbs.interfaces import ILoveThumbsDontYou
from sg.questions import _


class ISGQuestionsLayer(IDefaultBrowserLayer):
    """ Browser layer for sg.questions """


class IQuestion(form.Schema):
    """ A content-type for source code snippets. """
    title = schema.TextLine(title=_(u"Your question"), required=True)
    question = RichText(title=_(u"A description for the question"), required=False)

alsoProvides(IQuestion, ILoveThumbsDontYou)

class View(dexterity.DisplayForm):
    grok.context(IQuestion)
    grok.require('zope2.View')
    grok.layer(ISGQuestionsLayer)


class CommentsRatingViewlet(CommentsViewlet, grok.Viewlet):
    """ This viewlet is added to rate the comment """
    grok.context(IQuestion)
    grok.viewletmanager(IBelowContent)
    grok.layer(ISGQuestionsLayer)
    grok.name('plone.comments')

    index = ViewPageTemplateFile('question_templates/rating_viewlet.pt')

    
