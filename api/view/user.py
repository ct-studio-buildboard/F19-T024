from model.user import User


def getUserById(id) :
    a = User(id)
    return a.toJSON()