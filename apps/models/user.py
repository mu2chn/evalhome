from datetime import datetime
from apps import mongo
import uuid

class User:
    def __init__(self, lat: float, lng: float, cookie=None):
        self.lat = lat
        self.lng = lng
        self.date = int(datetime.now().strftime('%s'))
        self.cookie = cookie
        self.point = None
        self.uid = str(uuid.uuid4())

    def setPoint(self, score):
        self.point = score['total_points']
        scorelist = []
        for s in score["scores"]:
            scorelist.append({"tag": s.tag, "point": s.total, "uid": self.uid})
        mongo.db.LOG.insert_many(scorelist)
        self.insert()

    def dump(self):
        return self.__dict__

    def insert(self):
        mongo.db.USER.insert_one(self.dump())