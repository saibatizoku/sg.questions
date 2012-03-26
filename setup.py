from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='sg.questions',
      version=version,
      description="Content type for Plone 4> that allows user to ask questions, answer and rate those answers.",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='plone',
      author='Joaquin Rosales',
      author_email='globojorro@gmail.com',
      url='https://github.com/saibatizoku/sg.questions',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['sg'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'setuptools',
        # -*- Extra requirements: -*-
        'Plone',
        # -+- for comments and discussions -+-
        'collective.autoresizetextarea',
        'plone.formwidget.captcha',
        'plone.formwidget.recaptcha',
        'collective.z3cform.norobots',
        'plone.app.discussion',
        # -+- Like/Don't like -+-
        'cioppino.twothumbs',
        'plone.app.dexterity',
        'plone.app.referenceablebehavior',
        'collective.autopermission',
        ],
      extras_require={
        'test': ['plone.app.testing'],
        },
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
