class User:

    def __init__(self, cookie: str, date: int, lat: float, lng: float):
        self.lat = lat
        self.lng = lng
        self.date = date
        self.cookie = cokie
        self.point = None

    def setPoint(self, point: int):
        self.point = point