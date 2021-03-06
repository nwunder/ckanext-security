from setuptools import setup, find_packages

version = '0.1.0'

setup(
    name='ckanext-security',
    version=version,
    description='Various security patches for CKAN',
    long_description='',
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='Data.govt.nz',
    author_email='info@data.govt.nz',
    url='https://www.data.govt.nz',
    license='',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.security'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'repoze.who-use-beaker',
        'pylibmc'
    ],
    dependency_links=[
        'git+https://github.com/kaukas/repoze.who-use_beaker.git@8ec4cea#egg=repoze.who-use-beaker-0.4'
    ],
    entry_points=\
    """
    [ckan.plugins]
    security=ckanext.security.plugin:CatalystSecurityPlugin
    """,
)
