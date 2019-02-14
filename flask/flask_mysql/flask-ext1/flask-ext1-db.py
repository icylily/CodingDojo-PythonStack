from flask import Flask, request, g
from flask.ext.restful import Api, Resource
import sqlite3

app = Flask(__name__)
api = Api(app)

@app.before_request
def before_request():
    g.db = sqlite3.connect('db/users.db')

@app.teardown_request
def teardown_request(exception):
    g.db.close()

class User(Resource):
    def get(self, user_id):
        cur = g.db.execute('select id, name, age from users where id=?', user_id)
        users = [dict(id=row[0], name=row[1], age=row[2]) for row in cur.fetchall()]
        return users[0]

    def delete(self, user_id):
        user = self.get(user_id)
        g.db.execute('delete from users where id=?', user_id)
        g.db.commit()
        return user

    def put(self, user_id):
        g.db.execute('update users set name=?, age=? where id=?', [request.form['name'], request.form['age'], user_id])
        g.db.commit()
        return self.get(user_id)

class UserList(Resource):
    def get(self):
        cur = g.db.execute('select id, name, age from users')
        users = [dict(id=row[0], name=row[1], age=row[2]) for row in cur.fetchall()]
        return users

    def post(self):
        g.db.execute('insert into users (name, age) values (?, ?)', [request.form['name'], request.form['age']])
        g.db.commit()
        return {'message':'Successful'},201

api.add_resource(UserList, '/users')
api.add_resource(User, '/users/<user_id>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)