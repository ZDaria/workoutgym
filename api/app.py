#!flask/bin/python
from flask import abort, Flask, jsonify

from db.users import get, get_user_by_id
app = Flask(__name__)


@app.route('/workoutgym/api/v1.0/users', methods=['GET'])
def get_users():
    users = get()
    if len(users) == 0:
        abort(404)
    return users


@app.route('/workoutgym/api/v1.0/users/<int:user_id>', methods=['GET'])
def get_users_by_id(user_id):
    users = get_user_by_id(user_id)
    if len(users) == 0:
        abort(404)
    return users


if __name__ == '__main__':
    app.run(debug=True)