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

    from rng_to_form.rng import RNG
    from rng_to_form.form_maker import make_form, make_tree, set_in_nested_dict, order_dicts

    """
    List of rng tools
    """

    # Creates an RNG object to use rng tools
    rng = RNG(file="/path/to/my/rng/file.rng", target="ArchiveTransfer")

    # 1 - Tools to make the form

    # Builds an html form in a string
    generated_form = make_form(rng)
    # Returns elements order
    order = rng.find_definitions()
    # From the specified element, returns all nested orders
    form_root = rng.get_form_root(root_name="ArchiveTransfer")

    # 2 - Tools to get data from the form

    # Generates a dict of dicts from dot separated keys. Result will be : {'a': {'c': {}, 'b': {}}, 'b': {'d': {}, 'e': {'b': {}, 'a': {}}}}
    data = {'a.b': 1, 'a.c': 2, 'b.d' : 1, 'b.e.a': 1, 'b.e.b': 2}
    tree = make_tree(data)
    # Makes a nested python object from the form data. It modifies "tree"
    set_in_nested_dict(tree, data)
    # Builds the final python object with all ordered elements
    order = rng.find_definitions()
    all_data = {rng.get_form_root(root_name="ArchiveTransfer"): tree}
    final = order_dicts(all_data, ordered=order)

    # 3 - Tools to get data from the form

    # Flattens nested dicts into a single level dict. Result will be : {'a.b': 1, 'a.c': 2, 'b.d' : 1, 'b.e.a': 1, 'b.e.b': 2}
    dp = dict_path({'a': {'b': 1, 'c': 2}, 'b': {'d': 1, 'e': {'a': 1, 'b': 2}}})


Authors
-------

* Geoffroy : https://github.com/orgs/unistra/people/geoffroybeck
* Morgan : https://github.com/orgs/unistra/people/dotmobo
