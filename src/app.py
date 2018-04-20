from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from src.security import authenticate, identity
from src.user import UserRegister
from src.item import Item, ItemList

app = Flask(__name__)
app.secret_key = 'secret'
api = Api(app)

jwt = JWT(app, authenticate, identity)  # creates new end point /auth

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    app.run(port=9090, debug=True)
