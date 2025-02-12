#from app import create_app

#webapp = create_app()

from app import main as get_weather
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', method=['GET','POST'])
def index():
    if request.method == 'POST':
        city = request.form['cityName']
        state = request.form['stateName']
        country = request.form['countryName']
        print(get_weather(city, state, country))
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)