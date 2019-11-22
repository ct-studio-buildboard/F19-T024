from idea import Idea
from view.user import getUserById


def getIdeaForUser(user_id, city, country) :
    #get categories by user_id
    user = getUserById(user_id)

    #do system call and pass categories to model

    a = Idea(city+", "+country, user.name + " in boxing pose", "low angle", "black and white", user.equipment[0])
    return a