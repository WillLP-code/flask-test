from flask import Blueprint

# Blueprint files tell Flask that it's the blueprint for our website
auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return "<p>Login</p>"

@auth.route('logout')
def logout():
    return "<p>Logout</p>"

@auth.route('signup')
def signup():
    return "<p>Sign-up</p>"