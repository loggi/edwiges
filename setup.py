""" Setup file.
"""
import os
from setuptools import setup, find_packages

REQUIREMENTS = [
    'cornice',
    'colander',
    'PasteScript',
    'waitress',
    'logmatic-python',
]


here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.rst')) as f:
    README = f.read()


setup(
    name='edwiges',
    version='0.1.0',
    description='A stupidly simple email REST service.',
    long_description=README,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application"
    ],
    keywords="web services",
    author='Gabriela Surita',
    author_email='gsurita@loggi.com',
    url='https://github.com/loggi/edwiges',
    licence='Apache Licence v2.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=REQUIREMENTS,
    entry_points="""\
    [paste.app_factory]
    main = edwiges:main
    """,
    paster_plugins=['pyramid'],
)
