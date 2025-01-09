from flask import Blueprint, render_template

approutes = Blueprint('approutes', __name__)

@approutes.route('/')
def home():
    return render_template("home.html")