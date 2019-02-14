from flask import Flask
from flask.ext.restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)

USER_LIST = {
    1: {'name':'Michael'},
    2: {'name':'Tom'},
}

parser = reqparse.RequestParser()
parser.add_argument('name', type=str)

def abort_if_not_exist(user_id):
    if user_id not in USER_LIST:
        abort(404, message="User {} doesn't exist".format(user_id))

class User(Resource):
    def get(self, user_id):
        abort_if_not_exist(user_id)
        return USER_LIST[user_id]

    def delete(self, user_id):
        abort_if_not_exist(user_id)
        del USER_LIST[user_id]
        return '', 204

    def put(self, user_id):
        args = parser.parse_args(strict=True)
        USER_LIST[user_id] = {'name': args['name']}
        return USER_LIST[user_id], 201

class UserList(Resource):
    def get(self):
        return USER_LIST

    def post(self):
        args = parser.parse_args(strict=True)
        user_id = int(max(USER_LIST.keys())) + 1
        USER_LIST[user_id] = {'name': args['name']}
        return USER_LIST[user_id], 201

api.add_resource(UserList, '/users')
api.add_resource(User, '/users/<int:user_id>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)