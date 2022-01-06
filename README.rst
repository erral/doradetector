=================
Doraemon Detector
=================


.. image:: https://img.shields.io/pypi/v/doradetector.svg
        :target: https://pypi.python.org/pypi/doradetector

.. image:: https://img.shields.io/travis/erral/doradetector.svg
        :target: https://travis-ci.com/erral/doradetector

.. image:: https://readthedocs.org/projects/doradetector/badge/?version=latest
        :target: https://doradetector.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status




Python package to detect when ETB emits Doraemon


* Free software: GNU General Public License v3
* Documentation: https://doradetector.readthedocs.io.


Features
--------

* TODO


Usage
-----

How to use this module::
    >>> from doradetector import doradetector
    >>> results = doradetector.doradetector('2022-01-06')
    >>> results
    [{'channel': 'ETB-1',
    'date': '2022-01-06',
    'hour': ' 07:05',
    'title': '\r\n'
            '\t\t\t\t\t\r\n'
            '\t  \t\tDoraemon\t\t\t\t\t\t\t\t\t\t - Gorputzak trukatuta '},
    {'channel': 'ETB-3',
    'date': '2022-01-06',
    'hour': ' 07:00',
    'title': '\r\n'
            '\t\t\t\t\t\r\n'
            '\t  \t\tDoraemon\t\t\t\t\t\t\t\t\t\t - Gorputzak trukatuta '},
    {'channel': 'ETB-3',
    'date': '2022-01-06',
    'hour': ' 21:40',
    'title': '\r\n'
            '\t\t\t\t\t\t\t\r\n'
            '\t  \t\tDoraemon\t\t\t\t\t - Nobitaren energia '},
    {'channel': 'ETB-3',
    'date': '2022-01-06',
    'hour': ' 22:05',
    'title': '\r\n'
            '\t\t\t\t\t\t\t\r\n'
            '\t  \t\tDoraemon\t\t\t\t\t - Giza lokomotora '},
    {'channel': 'ETB-3',
    'date': '2022-01-06',
    'hour': ' 22:30',
    'title': '\r\n\t\t\t\t\t\t\t\r\n\t  \t\tDoraemon\t\t\t\t\t - Halloween '}]

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
