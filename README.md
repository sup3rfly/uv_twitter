This file gives the details about using the uv_twitter project which aims to verify the functionality of POST and GET endpoints of Twitter using tweepy Python module.

Setup instructions
------------------

Manual setup
------------

You will need the following:
* Python 2.7.x installed. [1]
* Tweepy Python plugin installed. [2]
* nose extension. [3]
* An active internet connection

Automatic setup
---------------
To avoid the manual setup, the tests can be run also in a docker container. You can get a preconfigured docker container them by pulling the following from docker hub:
$ docker pull alexgeorgescu/twittertest

NOTE: Docker needs to be installed on the host machine.


Run instructions
----------------
The tests can be found under the "test" folder. To run the tests simply run:
$ nosetests -s test_get.py
$ nosetests -s test_post.py


[1] - https://www.python.org/download/releases/2.7/
[2] - http://tweepy.readthedocs.io/en/v3.5.0/
[3] - https://nose.readthedocs.io/en/latest/
[4] - https://docs.docker.com/engine/installation/
