"""
Usage: python setup.py py2app
"""

from setuptools import setup

APP = ['space_invaders.py']
DATA_FILES = [('', ['images'])]
OPTIONS = {'iconfile': 'ship_icon.icns'}

setup(
    app = APP,
    data_files = DATA_FILES,
    options = {'py2app': OPTIONS},
    setup_requires = ['py2app']
)