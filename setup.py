#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = [
    "beautifulsoup4==4.10.0",
    "certifi==2021.10.8",
    "charset-normalizer==2.0.10",
    "idna==3.3",
    "requests==2.27.1",
    "soupsieve==2.3.1",
    "urllib3==1.26.7",
]

test_requirements = []

setup(
    author="Mikel Larreategi",
    author_email="mlarreategi@codesyntax.com",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="Python package to detect when ETB emits Doraemon",
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="doradetector",
    name="doradetector",
    packages=find_packages(include=["doradetector", "doradetector.*"]),
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/erral/doradetector",
    version="1.0.1",
    zip_safe=False,
)
