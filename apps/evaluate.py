from apps import wave, mongo
from apps.assess import PolynomialSpotFactor

def getData(tag, factor):
    collections = mongo.db.PLACE.find({"tag": tag})
    for spot in collections:
        factor.appendData(spot["name"], spot["lat"], spot["lng"], float(spot["rating"])/3)

superFactor = PolynomialSpotFactor("スーパー")
getData(1, superFactor)
wave.appendFactor(superFactor, 1.2)

