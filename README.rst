groIO
=======================

.. image:: https://travis-ci.org/HubLot/groio.svg?branch=master
   :target: https://travis-ci.org/HubLot/groio
.. image:: https://coveralls.io/repos/HubLot/groio/badge.svg?branch=master
   :target: https://coveralls.io/r/HubLot/groio?branch=master 



A library to handle the reading and writing of a gro file.


Usage
-----

.. code:: python

    import groIO

    #Read a gro file
    title, atoms, box = groIO.parse_file("filin.gro")

    #Write a gro file
    with open("filout.gro", "w") as f:
        for line in groIO.write_gro(title, output_atoms, box):
            print(line, end='', file=f)

    #Renumber the atoms to avoid number above 100 000
    atoms = groIO.renumber(atoms)


The function ``parse_file`` returns :

- ``title``: the title of the system as written on line 1 of the file  as a string
- ``atoms``: a list of atom, each atom is stored as a dictionary
- ``box``: the box description as written on the last line as a string


Run tests
---------

Unit tests are available for g_remove_water in test_g_remove_water.py. You can
run them by simply execute test_g_remove_water.py::

    python test_groIO.py

The `nosetests python module <https://nose.readthedocs.org>`_ allows a smarter
display of the report by displaying test function outputs only when the test
fail. If you have nosetests installed you can run the test by typing::

    nosetests test_groIO.py
