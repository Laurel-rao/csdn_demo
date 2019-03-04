


from .models import User


def get_name():
    user = User.query.get(1)
    return user.username