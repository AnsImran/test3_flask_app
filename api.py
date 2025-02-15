from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
    {
        'name': 'beautiful store',
        'items': [
            {
                'name': 'flowers',
                'price': 100
            }
                 ]
    },
    {
        'name': 'beautiful store 2',
        'items': [
            {
                'name': 'books',
                'price': 100
            }
        ]
    }
]


@app.route('/')
def home():
    return "Hello to Api"


@app.route('/store', methods=['POST']) # in '/store', 'store' is an endpoint. 5000 e.g, port hogi.
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []                    # sirf store add kar rahay hain. items add nahi kar rahay
    }
    stores.append(new_store)           # stores ki list main appended
    return jsonify(new_store)          

@app.route('/store/<string:name>')     # <string:name>: store ka name. e.g: beautiful store, beautiful store2 and beautiful store3 etc ...
def get_store_name(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'store not found'})

@app.route('/store')                   # by default, methods=['GET'] | # yahan is route par directly aaye hain. via POST nahi X.
def get_all_store_name():
    return jsonify({'stores': stores})

@app.route('/store/<string:name>/item', methods=['POST'])
def create_store_item(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': 'store not found'})

@app.route('/store/<string:name>/item')
def get_store_item(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store['items'])
    return jsonify({'message': 'store not found'})

app.run(port=5000)


