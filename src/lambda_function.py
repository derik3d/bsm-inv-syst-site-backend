"""
general handler for the flask app
"""
import awsgi
from app import app

def lambda_handler(event, context):
    """ flask connector """
    return awsgi.response(app, event, context)
