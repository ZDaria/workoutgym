from .models import User


def get():
    users = User.query.all()
    return users


def get_user_by_id(user_id):
    users = User.query.filter(User.id == user_id)
    return users.firstname
