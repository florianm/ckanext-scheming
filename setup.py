from setuptools import setup, find_packages
import sys, os

version = '1.0.0'

setup(
    name='ckanext-scheming',
    version=version,
    description="Easy, sharable custom CKAN schemas",
    long_description="""Fork by Dept Parks & Wildlife, Western Australia
    """,
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='Government of Canada, Government of Western Australia',
    author_email='ian@excess.org, Florian.Mayer@dpaw.wa.gov.au',
    url='https://github.com/open-data/ckanext-scheming',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points=\
    """
    [ckan.plugins]
    scheming_datasets=ckanext.scheming.plugins:SchemingDatasetsPlugin
    scheming_groups=ckanext.scheming.plugins:SchemingGroupsPlugin
    scheming_organizations=ckanext.scheming.plugins:SchemingOrganizationsPlugin
    scheming_test_subclass=ckanext.scheming.tests.plugins:SchemingTestSubclass

    [paste.paster_command]
    scheming=ckanext.scheming.commands:SchemingCommand
    """,
)
