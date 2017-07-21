Edwiges
=======

.. image:: https://pbs.twimg.com/profile_images/1361293504/coruja.jpg


Running locally:
----------------

.. code-block::
    
    EDWIGES_PROVIDER_HOST=YOUR_HOST
    EDWIGES_PROVIDER_USERNAME=YOUR_USER
    EDWIGES_PROVIDER_PASSWORD=YOUR_PASSWORD
    
    python setup.py develop
    pserve edwiges.ini  --reload

.. note::
    
    You can also set the provider information on your .ini file.

With docker:
------------
.. code-block::
 
    EDWIGES_PROVIDER_HOST=YOUR_HOST
    EDWIGES_PROVIDER_USERNAME=YOUR_USER
    EDWIGES_PROVIDER_PASSWORD=YOUR_PASSWORD
    
    docker-compose up
