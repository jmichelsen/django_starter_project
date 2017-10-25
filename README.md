# django_starter_project

Clone this repo to get a starter project for Django.
Config is where repo-wide config goes including the various settings files for django.
Common is a django app that contains models, views, and utilities, that are shared across all other apps within the project.

To add your own django apps to the project, use command `django-admin startapp {your_app_name}`

Then hook your urls into the `config/urls.py` file and add your new app to the `INSTALLED_APPS` in your `config/settings/base.py` file
