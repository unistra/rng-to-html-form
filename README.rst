rng-to-html-form
================

Requirements
------------

* python 3.4
* lxml 3.4.4

Install
-------

.. code:: bash

    pip install rng-to-html-form

Usage
-----

Takes an rng file and makes an html form :

.. code:: python

    rng = RNG(file=profile.file, target="ArchiveTransfer")
    generated_form = make_form(rng)

Authors
-------

* Geoffroy : https://github.com/orgs/unistra/people/geoffroybeck
* Morgan : https://github.com/orgs/unistra/people/dotmobo
