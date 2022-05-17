#!flask/bin/python
from flask import abort, Flask, jsonify

app = Flask(__name__)


# POST - used to receive data
# GET - used to send data back only


# POST ../exercise data: {name:}
@app.route('/workoutgym/api/v1.0/exercise', methods=['POST'])
def create_exercise(exercise):
    pass


# GET ../exercise/<string: name>
@app.route('/workoutgym/api/v1.0/exercise/<string:name>')
def get_exercise(exercise):
    pass


# GET ../exercise
@app.route('/workoutgym/api/v1.0/exercise')
def get_exercises(exercise):
    pass
