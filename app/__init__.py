from flask import Flask
# from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
import requests

load_dotenv('.env')

api_key = os.getenv('API_KEY')

# app = Flask(__name__)
# api = Api(app)

def getWeather(city_name, state_code, country_code, API_key):
    resp = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={API_key}").json()
    data = resp[0]
    name, lat, lon = data.get('name'), data.get('lat'), data.get('lon')
    return name, lat, lon
    
print(getWeather('Chicago','IL','US',api_key))

#if __name__ == '__main__':
#    app.run(debug=True)

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

