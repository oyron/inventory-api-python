import os
from flask import Flask, request, jsonify, send_file, make_response
from flaskr.book_inventory import BookInventory

app = Flask(__name__)
app.config["DEBUG"] = True

book_inventory = BookInventory()


@app.route('/api/books', methods=['GET'])
def api_get_books():
    return jsonify(book_inventory.get_all_books())


@app.route('/api/books/<book_id>', methods=['GET'])
def api_get_book(book_id):
    return jsonify(book_inventory.get_book(book_id))


@app.route('/api/books', methods=['POST'])
def api_add_book():
    body = request.get_json()
    book = book_inventory.add_book(body['author'], body['title'])
    return jsonify(book), 201


@app.route('/api/books/<book_id>', methods=['PUT'])
def api_update_book(book_id):
    if not book_inventory.has_book(book_id):
        return 'Book with id {} not found'.format(book_id), 404
    body = request.get_json()
    book = book_inventory.update_book(book_id, body['author'], body['title'])
    return jsonify(book), 201


@app.route('/api/books/<book_id>', methods=['DELETE'])
def api_delete_book(book_id):
    if not book_inventory.has_book(book_id):
        return 'Book with id {} not found'.format(book_id), 404
    book_inventory.delete_book(book_id)
    return "", 204


@app.route('/')
def send_index():
    return send_file('static/index.html')


@app.route('/terms.html')
def send_static(path):
    return send_file('static/terms.html')


@app.route('/openapi.yaml')
def send_openapi():
    response = make_response(send_file('static/openapi.yaml'))
    response.headers['content-type'] = 'text/yaml; charset=UTF-8'
    return response


port = int(os.environ.get("PORT", 3100))
app.run(host="0.0.0.0", port=port)