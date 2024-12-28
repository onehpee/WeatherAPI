from flask import Blueprint, render_template

approutes = Blueprint('route', __name__)

@approutes.route('/')
def home():
    return render_template("home.html")