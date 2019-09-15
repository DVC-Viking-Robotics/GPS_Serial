.. image:: https://readthedocs.org/projects/gps-serial/badge/?version=latest
    :target: https://gps-serial.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

Introduction
============

Yet another GPS NMEA sentence parser, but this time with the threading module for expediting data parsing in background running threads. This was developed for & tested on the Raspberry PI.

Dependencies
============

This library requires the `py-serial library <https://pypi.org/project/pyserial/>`_

Installation
============

Currenty, there is no plan to deploy this single module library to pypi. but you can easily install this library using the following commands:

.. code-block:: shell

    git clone https://github.com/DVC-Viking-Robotics/GPS_Serial.git
    cd GPS_Serial
    python3 setup.py install

The previous commands should automatically install the `py-serial library <https://pypi.org/project/pyserial/>`_. However, if you get import errors related to the ``serial`` module, make sure the `py-serial library <https://pypi.org/project/pyserial/>`_ is install via:

.. code-block:: shell

    pip3 install pyserial

Some cases may require the commands beginning with ``python3`` or ``pip3`` be prefixed with ``sudo``.

What Is My Serial Device's Port Address?
========================================

If you're going to use the GPIO pins, ``RX`` and ``TX``, you must ensure that the ``serial`` interface is enabled by running:

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
