
.. image:: https://gps-serial.readthedocs.io/en/latest/?badge=latest
    :target: http://gps-serial.rtfd.io/
    :alt: Documentation Status

GPS Serial Library
==================

Yet another GPS NMEA sentence parser, but this time with the threaded module for expediting data parsing in background running threads. This was developed for & tested on the Raspberry PI.

Dependencies
============

This library requires the `py-serial library <https://pypi.org/project/pyserial/>`_

Installation
==============

Currenty, there is no plan to deploy this single module library to pypi.
Instead, make sure the `py-serial library <https://pypi.org/project/pyserial/>`_ is install via:

.. code-block:: shell

    pip3 install pyserial

Some cases may require the command be prefixed with ``sudo `` or appended with `` --user``.

Additionally, if you're going to use the GPIO pins, ``RX`` and ``TX``, you must ensure that the ``serial`` interface is enabled by running:

.. code-block:: shell

    sudo raspi-config

.. important:: make sure that the ``serial console`` feature is disabled. Otherwise, any data sent or received over these GPIO pins will be forwarded to a TTY console session if ``serial console`` feature is enabled (meaning this library will not be able to access the GPS module data).

It is worth noting that the port address for the GPIO serial pins is ``/dev/ttyS0``. If you are using a USB connection, the address can be looked up using the py-serial's tools module:

.. code-block:: shell

    python3 -m serial.tools.list_ports

You can then test which port in the outputted list is the GPS module by entering:

.. code-block:: shell

    python3 -m serial.tools.miniterm /dev/ttyS0

where you replace the ``/dev/ttyS0`` part with the address you're testing. To exit the miniterm application use ``ctrl+[``
