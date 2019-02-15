




def get_name(User):
    user = User.query.get(1)
    return user.username