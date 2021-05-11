#~um-mid-flask/app.py
#author Shakir

from flask import Flask, request, Response, jsonify
from database.db import initialize_db
from database.models import Books

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
	'db' : 'shakir',
    'host': 'localhost',
	'port' : 27017
}

initialize_db(app)

#this method returns a welcome note
@app.route('/')
def welcome():
    return {'welcome': 'um-mid-flask/app'}

#this method returns all books
@app.route('/books', methods=['GET'])
def get_all_books():
    book = Books.objects()
    if not book:
	    #book not found, return error
        return jsonify({'error': 'no books found!'})
    else:
        return jsonify(book.to_json())

#this method returns a book searched by id
@app.route('/books/<id>', methods=['GET'])
def get_book_by_id(id):
    book = Books.objects(id=id).first()
    if not book:
	    #book not found, return error
        return jsonify({'error': 'invalid book id!'})
    else:
        return jsonify(book.to_json())

#this method create a new book
@app.route('/books', methods=['POST'])
def add_book():
    body = request.get_json()
	#extracting book data from request
    book = Books(**body).save()
    return jsonify(book.to_json())

#this method update a book
@app.route('/books/<id>', methods=['PUT'])
def update_book(id):
    body = request.get_json()
    book = Books.objects(id=body['id']).first()
    if not book:
	    #book not found, return error
        return jsonify({'error': 'invalid book update request!'})
    else:
        book.update(**body)
        return jsonify(book.to_json())

#this method delete a book
@app.route('/books/<id>', methods=['DELETE'])
def delete_book(id):
    body = request.get_json()
    book = Books.objects(id=id).first()
    if not book:
	    #book not found, return error
        return jsonify({'error': 'invalid book delete request!'})
    else:
        book.delete()
    return jsonify({'success': 'book delete complete!'})

if __name__ == "__main__":
    app.run(debug=True)
