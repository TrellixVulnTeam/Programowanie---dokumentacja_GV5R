from datetime import timedelta

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from user import UserRegister
from item import Item, Items

app = Flask(__name__)
app.secret_key = 'wiktor'
api = Api(app)
app.config['JWT_AUTH_URL_RULE'] = '/login'

jwt = JWT(app, authenticate, identity) # /auth

app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=1800)

@jwt.auth_response_handler
def customized_response_handler(access_token, identity):
    return {
                        'access_token': access_token.decode('utf-8'),
                        'user_id': identity.id
                   }
@jwt.jwt_error_handler()
def customized_error_handler(error):
    return {
                       'message': error.description,
                       'code': error.status_code
                   }, error.status_code

api.add_resource(Item, '/item/<string:name>')
api.add_resource(Items, '/items')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
