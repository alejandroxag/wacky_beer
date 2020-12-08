from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='wacky_beer',
    url='https://github.com/alejandroxag/wacky_beer/',
    author='Team Wacky',
    author_email='',
    # Needed to actually package something
    packages=['wacky_beer'],
    # Needed for dependencies
    install_requires=['requests', 'bs4', 'pandas'],
    # *strongly* suggested for sharing
    version='0.1.0',
    # The license can be anything you like
    license='MIT',
    description='Group Project for the Data Focused Python Course. Beer information retrieval application.',
    package_data={'': ['data/*.csv']},
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)