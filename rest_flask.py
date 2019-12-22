import os
from flask import Flask, jsonify, request,url_for
app = Flask(__name__)
@app.route('/orders', methods=['GET'])
def getOrders():
    filename = os.path.join('/Users/tsandesfernandes/Documents/ifood', 'pedidos.JSON')
    with open(filename) as file:
        data = file.read()
    return jsonify(data)

@app.route('/toprestaurant', methods=['GET'])
def top10():
    filename = os.path.join('/Users/tsandesfernandes/Documents/ifood', 'top10.JSON')
    with open(filename) as file:
        data = file.read()
    return jsonify(data)
if __name__ == '__main__':
    app.run(debug=True)