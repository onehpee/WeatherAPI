from flask import Blueprint

approutes = Blueprint('route', __name__)

@approutes.route('/')
def home():
    return "<h1>Test</h1>"