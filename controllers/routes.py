from flask_restful import Api, Resource, reqparse
from flask_jwt_extended import jwt_required, create_access_token
from datetime import timedelta
from models.user_model import User
from models.book_model import Book
from flask import Blueprint, request, jsonify
from controllers.extension import db

routes_bp = Blueprint('routes_bp', __name__)
api = Api(routes_bp)

# Parser for Book data
book_parser = reqparse.RequestParser()
book_parser.add_argument('title', required=True, help="Title cannot be blank")
book_parser.add_argument('author', required=True)
book_parser.add_argument('isbn', required=True)
book_parser.add_argument('price', type=float, required=True)
book_parser.add_argument('quantity', type=int, required=True)

class BookList(Resource):
    @jwt_required()
    def get(self):
        books = Book.query.all()
        return jsonify([book.serialize() for book in books])

    @jwt_required()
    def post(self):
        args = book_parser.parse_args()
        new_book = Book(
            title=args['title'], 
            author=args['author'], 
            isbn=args['isbn'], 
            price=args['price'], 
            quantity=args['quantity']
        )
        db.session.add(new_book)
        db.session.commit()
        return new_book.serialize(), 201

class BookResource(Resource):
    @jwt_required()
    def get(self, isbn):
        book = Book.query.filter_by(isbn=isbn).first()
        if book:
            return jsonify(book.serialize())
        return {'message': 'Book not found'}, 404

    @jwt_required()
    def put(self, isbn):
        args = book_parser.parse_args()
        book = Book.query.filter_by(isbn=isbn).first()
        if book:
            book.title = args['title']
            book.author = args['author']
            book.price = args['price']
            book.quantity = args['quantity']
            db.session.commit()
            return jsonify(book.serialize())
        return {'message': 'Book not found'}, 404

    @jwt_required()
    def delete(self, isbn):
        book = Book.query.filter_by(isbn=isbn).first()
        if book:
            db.session.delete(book)
            db.session.commit()
            return {'message': 'Book deleted'}
        return {'message': 'Book not found'}, 404
    
api.add_resource(BookList, '/books')
api.add_resource(BookResource, '/books/<string:isbn>')


@routes_bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'Username and password are required!'}), 400

    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return jsonify({'message': 'Username already exists'}), 409

    new_user = User(username=username)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User created successfully'}), 201


@routes_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        access_token = create_access_token(identity=username, expires_delta=timedelta(days=1))
        return jsonify(access_token=access_token)

    return jsonify({'message': 'Invalid username or password'}), 401