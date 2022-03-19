from db import db_session
from models import User

user = User.query.first()
user.firstname = "Ivan"
db_session.commit()
