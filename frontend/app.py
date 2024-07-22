#!/usr/bin/env python3

from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

# Load configuration
app.config.from_pyfile('config.py')

# Define the route for the main page
@app.route('/')
def index():
    try:
        # Get the stock data from the API
        response = requests.get(app.config['STOCK_API_URL'])
        response.raise_for_status()
        if response.status_code != 200:
            raise requests.RequestException(f"Error: {response.status_code}")
        stock_data = response.json()
        available_items = stock_data.get('available', 'N/A')
    except requests.RequestException as e:
        print(f"Error retrieving stock data: {e}")
        available_items = 'N/A'

    return render_template('index.html', available_items=available_items)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)