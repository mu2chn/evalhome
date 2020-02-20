from apps import wave, mongo
from apps.assess import PolynomialSpotFactor
from apps.models import Spot

def getData(tag, factor):
    collections = mongo.db.PLACE.find({"tag": tag})
    for spot in collections:
        factor.appendData(spot["name"], spot["lat"], spot["lng"], float(spot["rating"])/3)

for i in [
    ["スーパー", Spot.SUPERMARKET],
    ["コンビニ", Spot.CONVINIENCESTOROE],
    ["ラーメン", Spot.NOODLE],
    ["銭湯", Spot.SENTO],
    ["パン屋", Spot.BAKERY],
    ["薬局", Spot.DRAGSTORE],
    ["銀行", Spot.BANK],
    ["車高", Spot.CARSCHOOL]
]:
    factor = PolynomialSpotFactor(i[0])
    getData(i[1], factor)
    wave.appendFactor(factor, tag=i[1], weight=1.2)

