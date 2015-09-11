groIO
=======================

.. image:: https://travis-ci.org/HubLot/groio.svg?branch=master
   :target: https://travis-ci.org/HubLot/groio
.. image:: https://coveralls.io/repos/HubLot/groio/badge.svg?branch=master&service=github
  :target: https://coveralls.io/github/HubLot/groio?branch=master


A library to handle the reading and writing of a gro file.


Installation
------------

    pip install groio

Usage
-----

.. code:: python

    import groio

    #Read a gro file
    title, atoms, box = groio.parse_file("filin.gro")

    #Write a gro file
    with open("filout.gro", "w") as f:
        for line in groio.write_gro(title, output_atoms, box):
            print(line, end='', file=f)

    #Renumber the atoms to avoid number above 100 000
    atoms = groio.renumber(atoms)


The function ``parse_file`` returns :

- ``title``: the title of the system as written on line 1 of the file  as a string
- ``atoms``: a list of atom, each atom is stored as a dictionary
- ``box``: the box description as written on the last line as a string


Run tests
---------

Unit tests are available through `nosetests python module <https://nose.readthedocs.org>`_.
    nosetests tests/test_groio.py
