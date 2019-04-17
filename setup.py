# This file is adapted from the BSD licensed file from Nubia setup.py
# The file is available at: 
# https://github.com/facebookincubator/python-nubia/blob/537e6c44834f7c4ecb7b037d7b28edf0bf49925e/setup.py

import ast
import re
import setuptools
import sys

# To use a consistent encoding
from codecs import open
from os import path
from pathlib import Path

assert sys.version_info >= (3, 7, 0), "pelcan-cms requires Python 3.7+"

try:
    from pipenv.project import Project
    from pipenv.utils import convert_deps_to_pip

except ImportError:
    print("pipenv has to be installed, use 'pip3 install pipenv'", file=sys.stderr)
    sys.exit(1)


here = Path(__file__).parent


def get_long_description() -> str:
    with open(path.join(here, "README.md"), "r", encoding="utf-8") as file:
        return file.read()


def get_version() -> str:
    init_location = here / "pelican_cms/__init__.py"

    _version_re = re.compile(r"__version__\s+=\s+(?P<version>.*)")

    with open(init_location, "r", encoding="utf8") as init_file:
        match = _version_re.search(init_file.read())

        if match is not None:
            version = match.group("version") i
        else:
            version = '"unknown"'

    return str(ast.literal_eval(version))


pipfile = Project(chdir=False).parsed_pipfile
requirements = convert_deps_to_pip(pipfile["packages"], r=False)
test_requirements = convert_deps_to_pip(pipfile["dev-packages"], r=False)

setuptools.setup(
    name="pelican-cms",
    version=get_version(),
    author="Ezequiel Leonardo Castaño",
    author_email="elcg@gmx.com",
    description="A framework for building beautiful shells",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    keywords="pelican blog static-site framework cms",
    url="https://github.com/ELC/pelican-cms",
    packages=setuptools.find_packages(exclude=["docs", "tests"]),
    python_requires=">=3.7",
    install_requires=requirements,
    classifiers=(
        "Development Status :: 1 - Planning",
        "Environment :: Web Environment",
        "Framework :: Flask",
        "Framework :: Pelican",
        "Intended Audience :: End Users/Desktop",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Content Management System",
    ),
)