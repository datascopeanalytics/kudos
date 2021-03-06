# kudos

A crappy implementation of a good idea: give colleagues continuous kudos
throughout the year

### Getting started

1. `vagrant up` to start the virtual machine

2. `fab dev provision` to install all of the prerequisite software

3. `./manage.py migrate` to load the data into the database

4. `./manage.py createsuperuser` to create a superuser account

5. Follow [the
   instructions](http://django-allauth.readthedocs.org/en/latest/providers.html#google)
   for registering social authentication via google using the `allauth` app.

6. Create a user by running the server with `fab dev serve` and logging in for
   the first time:

7. If you're so inclined, you can simulate a whole buncha kudos by running
   `./manage.py simulate_kudos` (kudos messages courtesy of [this heartfelt
   site](http://smstosay.com/thanks-sms/20-sms-to-say-thank-you-sms-to-say-thanks/)).
   To do this you'll need to `vagrant ssh` and then `cd web/ && ./manage simulate_kudos`.

### Internals

This project is provisioned with @gabegaster's
[FabTools_StartKit](https://github.com/gabegaster/FabTools_StartKit) and is
built off of @xenith's
[django-base-template](https://github.com/xenith/django-base-template).
