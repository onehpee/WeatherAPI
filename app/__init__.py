from flask import Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
import requests


app = Flask(__name__)
api = Api(app)

def getWeather(location, date1, date2, API_KEY):
    resp = requests.get("https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/[location]/[date1]/[date2]?key=YOUR_API_KEY")
        

if __name__ == '__main__':
    app.run(debug=True)

# def create_app():
#     app = Flask(__name__, template_folder='blueprints/auth/templates/auth')
#     app = Api(app)
#     #encrypt and secure cookies and sessions data
#     app.config['SECRET_KEY'] = 'chama'
    
#     from .routes import approutes
#     from .blueprints .auth .routes import auth_routes
    
#     app.register_blueprint(approutes, url_prefix='/')
#     app.register_blueprint(auth_routes, url_prefix= '/')
    
#     return app

