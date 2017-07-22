Edwiges
=======

**Under development**

Edwiges is a simple service written in Python/Pyramid/Cornice that can take a REST JSON request and use it to send emails. It does supports attachments and metainfo. 

*As long term goals we want Edwiges to be able to handle everything related to an email flow, such as consumable metrics, warnings, rendering templates, scheduling, retrying and so on.*

.. image:: https://pbs.twimg.com/profile_images/1361293504/coruja.jpg
   :scale: 50 %
   :align: right

Running locally:
----------------

.. code-block::
    
    export EDWIGES_PROVIDER_HOST=YOUR_HOST
    export EDWIGES_PROVIDER_USERNAME=YOUR_USER
    export EDWIGES_PROVIDER_PASSWORD=YOUR_PASSWORD
    
    python setup.py develop
    pserve edwiges.ini  --reload

.. note::
    
    You can also set the provider information on your .ini file.

With docker:
------------
.. code-block::
 
    export EDWIGES_PROVIDER_HOST=YOUR_HOST
    export EDWIGES_PROVIDER_USERNAME=YOUR_USER
    export EDWIGES_PROVIDER_PASSWORD=YOUR_PASSWORD
    
    docker-compose up
