from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='elevate.cynin.fixes',
      version=version,
      description="Cynin fixes for elevate",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='cynin, plone',
      author='Johannes Raggam',
      author_email='raggam-nl@adm.at',
      url='https://github.com/thet/elevate.cynin.fixes',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['elevate', 'elevate.cynin'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
         'collective.monkeypatcher',
      ],
      )
