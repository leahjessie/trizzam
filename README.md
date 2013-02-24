trizzam
=======

To develop trizzam, you need to install some things.

Install pip:
$ curl -O https://raw.github.com/pypa/pip/master/contrib/get-pip.py
$ sudo python get-pip.py

$ pip install Django

$ pip install --upgrade google-api-python-client

Install and start mongodb:
http://www.mongodb.org/downloads
Remember to make a directory for data
$ 'MONGOPATH'/bin/mongod --dbpath ~/'DATADIR'

Install mongoengine:
$ pip install mongoengine
