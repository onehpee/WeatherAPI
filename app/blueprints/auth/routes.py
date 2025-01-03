from flask import Blueprint, render_template

auth_routes = Blueprint('route', __name__)


@auth_routes.route('/login')
def login():
    return render_template("login.html", boolean="True")

@auth_routes.route("/logout")
def logout():
    return "<p>Logout</p>"

@auth_routes.route("/signup")
def sign_up():
    return render_template("sign_up.html")

