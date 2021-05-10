#~um-mid-flask/app.py

from flask import Flask, request, Response
from database.db import initialize_db
from database.models import Book

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
	'db' : 'your_database',
    'host': 'localhost',
	'port' : 27017
}

initialize_db(app)

@app.route('/')
def welcome():
    return {'welcome': 'um-mid-flask/app'}

@app.route('/books', methods=['GET'])
def get_all_books():
    book = Book.objects()
    if not book:
        return jsonify({'error': 'no books found!'})
    else:
        return jsonify(book.to_json())

@app.route('/books', methods=['POST'])
def add_book():
    body = request.get_json()
    book = Book(**body).save()
    return jsonify(book.to_json())

@app.route('/books/<id>', methods=['PUT'])
def update_book(id):
    body = request.get_json()
    book = Book.objects(id=body['id']).first()
    if not book:
        return jsonify({'error': 'invalid book update request!'})
    else:
        book.update(**body)
    return jsonify(book.to_json())

@app.route('/books/<id>', methods=['DELETE'])
def delete_book(id):
    body = request.get_json()
    book = Book.objects(id=body['id']).first()
    if not book:
        return jsonify({'error': 'invalid book delete request!'})
    else:
        book.delete()
    return jsonify({'success': 'book delete complete!'})

if __name__ == "__main__":
    app.run(debug=True)
