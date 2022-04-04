from .models import User


def get():
    users = User.query.first()
    return users.firstname


def get_user_by_id(user_id):
    users = User.query.filter(User.id == user_id)
    return users.firstname
