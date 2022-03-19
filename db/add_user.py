from db import db_session
from models import User

user = User(firstname="Иван", lastname="Иванов", age=26, weight=90, height=193,
            birthday="1996-03-18")
db_session.add(user)
db_session.commit()