import json

from model.location import Location


class User:

    def __init__(self, id):
        self.id = id
        self.getUserById(id)


    def getUserById(self, id):
        if id==1:
            self.name = "Irene"
            self.numberOfFollowers = 10000
            self.numberOfPictures = 30
            self.location =  Location("Barcelona", "Spain")
            self.topSkills = ["Animals", "Architecture"]
            self.equipment = ["NIKON D500", "PIXEL 3XL"]
        elif id ==2:
            self.name = "Camyll"
            self.numberOfFollowers = 1000
            self.numberOfPictures = 10
            self.location = Location("Michigan", "Detroit")
            self.topSkills = ["Nature", "Dogs"]
            self.equipment = ["NIKON D500", "PIXEL 3XL"]

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=False, indent=4)
