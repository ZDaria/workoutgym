from .models import User


def get():
    users = User.query.first()
    return users.firstname
