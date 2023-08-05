import pathlib
from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent

VERSION = '1.0.2'
PACKAGE_NAME = 'xtweet' 
AUTHOR = 'Francisco Griman'
AUTHOR_EMAIL = 'grihardware@gmail.com'
URL = 'https://github.com/fcoagz/pydolarvenezuela'

LICENSE = 'MIT'
DESCRIPTION = 'Es una biblioteca que te permite interactuar de manera eficiente con la API de Twitter.'
LONG_DESCRIPTION = (HERE / "README.md").read_text(encoding='utf-8')
LONG_DESC_TYPE = "text/markdown"

INSTALL_REQUIRES = [
      'requests',
      'cachetools'
      ]

CLASSIFIERS = [
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'
    ]

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESC_TYPE,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    install_requires=INSTALL_REQUIRES,
    license=LICENSE,
    packages=find_packages(),
    include_package_data=True,
    classifiers=CLASSIFIERS
)