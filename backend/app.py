from flask import Flask, jsonify

app = Flask(__name__)

# Mock stock data
stock_data = {
    "available": 150  # Example stock quantity
}

# Define the API endpoint to get stock data
@app.route('/api/v1/stock', methods=['GET'])
def get_stock():
    return jsonify(stock_data)

@app.route('/api/v2/secret', methods=['GET'])
def get_secret():
    return "You hit a secret API endpoint!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001, debug=True)