from flask import Blueprint

routes = Blueprint('route', __name__)

@routes.route('/')
def home():
    return "<h1>Test</h1>"