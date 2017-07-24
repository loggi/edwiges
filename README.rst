Edwiges
=======

**Under development!**

Edwiges is a simple service written in Python/Pyramid/Cornice
that can take a REST JSON request and use it to send emails using SMTP. 
It does supports attachments and metainfo.

The basic premise is that on a microservice architecture we don't want
all services to be able to send e-mails directly.
SMTP seems easy at first-glance, but it can get very tricky as you 
include more complex features. 
REST is idiomatic and easy to use in most languages, plus, by having
a separated service, you can get zero-cost monitoring and metrics.

*As long term goals we want Edwiges to be able to handle everything
related to an email flow, such as consumable metrics, warnings,
rendering templates, scheduling, retrying and so on.*

.. image:: https://pbs.twimg.com/profile_images/1361293504/coruja.jpg
   :scale: 50 %
   :align: right

Running locally:
----------------

Clone this repository and run:

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
   
   


.. code-block::
 
    export EDWIGES_PROVIDER_HOST=YOUR_HOST
    export EDWIGES_PROVIDER_USERNAME=YOUR_USER
    export EDWIGES_PROVIDER_PASSWORD=YOUR_PASSWORD
    
    docker-compose up


API Quick Reference
-------------------

*Note: these examples were performed using GMail, responses can change 
according to the provider. You may need to enable 
https://myaccount.google.com/lesssecureapps to use Edwiges with Gmail.*

**GET /  -  Server Test**

Request:

.. code-block::

   $ http -v get localhost:10085
   GET / HTTP/1.1
   Accept: */*
   Accept-Encoding: gzip, deflate
   Connection: keep-alive
   Host: localhost:10085
   User-Agent: HTTPie/0.9.9

Response:

.. code-block::

   HTTP/1.1 200 OK
   Content-Length: 62
   Content-Type: application/json
   Date: Sat, 22 Jul 2017 05:05:47 GMT
   Server: waitress
   X-Content-Type-Options: nosniff

   {
       "errors": [],
       "status": "2.0.0 OK s6sm4499738qki.44 - gsmtp"
   }
   
**POST /mail  -  Send Email**

Request:

.. code-block::

   $ echo '{"sender": "gabsurita@gmail.com", \
            "recipients": ["gabsurita@gmail.com"], \
            "subject": "Grrr", \
            "body": "Hello from edwiges"}' | http -v post localhost:10085/mail
   POST /mail HTTP/1.1
   Accept: application/json, */*
   Accept-Encoding: gzip, deflate
   Connection: keep-alive
   Content-Length: 122
   Content-Type: application/json
   Host: localhost:10085
   User-Agent: HTTPie/0.9.9

   {
       "body": "Hello from edwiges",
       "recipients": [
           "gabsurita@gmail.com"
       ],
       "sender": "gabsurita@gmail.com",
       "subject": "Grrr"
   }

Response:

.. code-block::

   HTTP/1.1 200 OK
   Content-Length: 139
   Content-Type: application/json
   Date: Sat, 22 Jul 2017 05:04:22 GMT
   Server: waitress
   X-Content-Type-Options: nosniff

   {
       "body": "Hello from edwiges",
       "recipients": [
           "gabsurita@gmail.com"
       ],
       "sender": "gabsurita@gmail.com",
       "status": "sent",
       "subject": "Grrr"
   }

