from db_connection import db_session
from models import User

user = User.query.first()
db_session.delete(user)
db_session.commit()
