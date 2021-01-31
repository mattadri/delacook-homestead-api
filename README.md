# delacook-homestead-api

This README outlines the details of collaborating on this Ember application.

## To Start the API  
* `source .env`
* Once in the enviroment run: `python run.py`

## Prod Run:
* source .env
* gunicorn --bind 0.0.0.0:5001 wsgi:application
