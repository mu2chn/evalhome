class Spot:
    
    def __init__(self, lat, lng, name, review=0.0):
        self.lat = lat
        self.lng = lng
        self.name = name
        self.review = review