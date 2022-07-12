#!flask/bin/python
from flask import abort, Flask, jsonify, request

from db.users import get, get_user_by_id
app = Flask(__name__)


# GET ../user/<string: firstname>
@app.route('/workoutgym/api/v1.0/user/<string:name>')
def get_user(firstname):
    users = get()
    return jsonify(users)


# GET ../user
@app.route('/workoutgym/api/v1.0/user')
def get_users():
    users = get()
    return jsonify(users)

'''
# POST ../user data: {firstname:, lastname:, age:, weight:, height:, birthday:}
@app.route('/user', method=['POST'])
def create_user():
    pass

# get
@app.route('/workoutgym/api/v1.0/user/<int:user_id>', methods=['GET'])
def get_users_by_id(user_id):
    users = get_user_by_id(user_id)
    if len(users) == 0:
        abort(404)
    return users

'''

if __name__ == '__main__':
    app.run(debug=True)