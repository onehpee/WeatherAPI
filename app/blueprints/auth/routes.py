from flask import Blueprint

auth_routes = Blueprint('route', __name__)

@auth_routes.route('/login')
def login():
    return "<p>Login</p>"

@auth_routes.route("/logout")
def logout():
    return "<p>Logout</p>"

@auth_routes.route("/signup")
def sign_up():
    return "<p>Sign up</p>"

