from flask import Blueprint

# Blueprint files tell Flask that it's the blueprint for our website
views = Blueprint('views', __name__)

# Name of view, route, and url to endpoint
@views.route('/')
# This fn runs whenever we go to this page
def home():
    return "<h1>Test</h1>"

