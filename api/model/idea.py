import json


class Idea:

    def __init__(self, location, idea, angle, light, camera):
        self.location = location
        self.idea = idea
        self.angle = angle
        self.light = light
        self.camera = camera


    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=False, indent=4)
