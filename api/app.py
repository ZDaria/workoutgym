#!flask/bin/python
from flask import abort, Flask, jsonify
from db.users import get
app = Flask(__name__)


@app.route('/workoutgym/api/v1.0/users', methods=['GET'])
def get_users():
    users = get()
    if len(users) == 0:
        abort(404)
    return users


@app.route('/workoutgym/api/v1.0/users/<int:users_id>', methods=['GET'])
def get_users(users_id):
    users = get()
    if len(users) == 0:
        abort(404)
    return users


if __name__ == '__main__':
    app.run(debug=True)