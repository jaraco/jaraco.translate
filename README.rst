.. image:: https://img.shields.io/pypi/v/jaraco.translate.svg
   :target: https://pypi.org/project/jaraco.translate

.. image:: https://img.shields.io/pypi/pyversions/jaraco.translate.svg

.. image:: https://github.com/jaraco/jaraco.translate/actions/workflows/main.yml/badge.svg
   :target: https://github.com/jaraco/jaraco.translate/actions?query=workflow%3A%22tests%22
   :alt: tests

.. image:: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json
    :target: https://github.com/astral-sh/ruff
    :alt: Ruff

.. .. image:: https://readthedocs.org/projects/PROJECT_RTD/badge/?version=latest
..    :target: https://PROJECT_RTD.readthedocs.io/en/latest/?badge=latest

.. image:: https://img.shields.io/badge/skeleton-2024-informational
   :target: https://blog.jaraco.com/skeleton

Natural language translation support using Google APIs.


pmxbot plugin
-------------

jaraco.translate supplies a plugin for `pmxbot
<https://github.com/yougov/pmxbot>`_.

To enable, simply install this package alongside pmxbot and
add your Google API key to the pmxbot config::

    Google API key: AB2x...

and then `!translate` away.
