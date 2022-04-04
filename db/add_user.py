from db_connection import db_session
from db.models import User

user = User(firstname="Кристина", lastname="Иванова", age=22, weight=60, height=193,
            birthday="2000-03-18")

db_session.add(user)
db_session.commit()