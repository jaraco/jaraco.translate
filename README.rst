.. image:: https://img.shields.io/pypi/v/skeleton.svg
   :target: https://pypi.org/project/skeleton

.. image:: https://img.shields.io/pypi/pyversions/skeleton.svg

.. image:: https://img.shields.io/travis/jaraco/skeleton/master.svg
   :target: https://travis-ci.org/jaraco/skeleton

.. .. image:: https://img.shields.io/appveyor/ci/jaraco/skeleton/master.svg
..    :target: https://ci.appveyor.com/project/jaraco/skeleton/branch/master

.. .. image:: https://readthedocs.org/projects/skeleton/badge/?version=latest
..    :target: https://skeleton.readthedocs.io/en/latest/?badge=latest

Natural language translation support using Google APIs.


pmxbot plugin
-------------

jaraco.translate supplies a plugin for `pmxbot
<https://github.com/yougov/pmxbot>`_.

To enable, simply install this package alongside pmxbot and
add your Google API key to the pmxbot config::

    google_translate_API_key: AB2x...

and then `!translate` away.
