from five import grok

from zope.interface import Interface
from zope import schema
from zope.component import getMultiAdapter
from Products.CMFCore.utils import getToolByName

from Products.CMFPlone.interfaces import IPloneSiteRoot
from plone.app.registry.browser import controlpanel

from sg.questions import _

try:
    # only in z3c.form 2.0
    from z3c.form.browser.textlines import TextLinesFieldWidget
except ImportError:
    from plone.z3cform.textlines import TextLinesFieldWidget

from z3c.form.browser.checkbox import CheckBoxFieldWidget

class ISGQuestionsSettings(Interface):
    """ Interface for the form on the control panel. """

class SGQuestionsSettingsEditForm(controlpanel.RegistryEditForm):
    grok.context(IPloneSiteRoot)
    grok.name("sg_questions_settings")
    grok.require("cmf.ManagePortal")

    schema = ISGQuestionsSettings
    label = _(u"SoftwareGuru Questions Settings") 
    description = _(u"Here you can modify the settings for SG Questions.")

    def updateFields(self):
        super(SGQuestionsSettingsEditForm, self).updateFields()

    def updateWidgets(self):
        super(SGQuestionsSettingsEditForm, self).updateWidgets()

class SGQuestionsSettingsControlPanel(controlpanel.ControlPanelFormWrapper):
    form = SGQuestionsSettingsEditForm
