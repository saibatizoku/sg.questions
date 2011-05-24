from five import grok
from zope import schema

from Products.CMFCore.interfaces import IContentish
from plone.app.layout.globals.interfaces import IViewView
from plone.app.layout.viewlets.interfaces import IBelowContent
from plone.app.discussion.interfaces import IDiscussionLayer
from plone.app.discussion.browser.comments import CommentsViewlet

from zope.publisher.interfaces.browser import IDefaultBrowserLayer

from plone.directives import form, dexterity
from plone.app.textfield import RichText

from sg.questions import _


class CommentsRatingViewlet(CommentsViewlet, grok.Viewlet):
    """ This viewlet is added to rate the comment """
    grok.context(IContentish)
    grok.viewletmanager(IBelowContent)
    grok.layer(IDiscussionLayer)
    grok.view(IViewView)

class ISGQuestionsLayer(IDefaultBrowserLayer):
    """ Browser layer for sg.questions """

class IQuestion(form.Schema):
    """ A content-type for source code snippets. """
    question = RichText(title=_(u"Ask a question"))

