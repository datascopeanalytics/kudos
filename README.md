# kudos

A crappy implementation of a good idea: give colleagues continuous kudos
throughout the year

### Getting started

1. `vagrant up` to start the virtual machine

2. `fab dev provision` to install all of the prerequisite software

3. `./manage.py migrate` to load the data into the database

4. Follow [the
   instructions](http://django-allauth.readthedocs.org/en/latest/providers.html#google)
   for registering social authentication via google using the `allauth` app. 

### Internals

This project is provisioned with @gabegaster's
[FabTools_StartKit](https://github.com/gabegaster/FabTools_StartKit) and is
built off of @xenith's
[django-base-template](https://github.com/xenith/django-base-template).
