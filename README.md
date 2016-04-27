
Elastic Beanstalk Docker template for Django
============================================

Boilerplate Docker template for Django 1.9+ running Python 3.4.+ on AWS's Elastic Beanstalk.

Assumes you have virtualenv and virtualenvwrapper installed.

Starting your project
---------------------

    $ mkdir /home/user/AWS/mysite.proj

    $ mkvirtualenv -a /home/user/AWS/mysite.proj mysite

    $ pip install Django

    $ export DJANGO_SETTINGS_MODULE=''

    $ django-admin.py startproject --template=https://github.com/kcoyner/django-AWS-beanstalk-docker-template/archive/master.zip mysite

    $ export DJANGO_SETTINGS_MODULE='mysite.settings'

    $ export PYTHONPATH=$PYTHONPATH:/home/user/AWS/mysite.proj/mysite

    $ django-admin check

Originally from a tutorial found at http://glynjackson.org/weblog/django-aws-elastic-beanstalk-docker-2/
