import googlemaps
import time
from pymongo import MongoClient

def getGeocodeOfPlace(place_name):
    result = gmaps.geocode(place_name)
    geocode = result[0]['geometry']['location']

    return geocode

def getPlacesAroundPivot(loc, facility_name):
    tmp = gmaps.places_nearby(location=loc,
                              keyword=facility_name,
                              radius='1000',
                              language='ja'
                             )
    places = tmp['results']

    while 'next_page_token' in tmp:
        token = tmp['next_page_token']
        while True:
            try:
                time.sleep(1) #トークンが有効になるまでに遅延が入る場合がある
                tmp = gmaps.places_nearby(page_token=token)
                break
            except googlemaps.exceptions.ApiError:
                pass

        places += tmp['results']

    print(str(len(places)) + '件取得')
    return places

def extractDataForMongo(places, id):
    data = []
    for place in places:
        dic = {}
        dic['id'] = place['place_id']
        dic['tag'] = id
        dic['name'] = place['name']
        dic['lat'] = place['geometry']['location']['lat']
        dic['lng'] = place['geometry']['location']['lng']
        dic['rating'] = place['rating']
        data.append(dic)

    return data


def main():
    mongo = MongoClient('localhost', 27017)
    db=mongo['evalhome']
    db.PLACE.create_index('id', unique=True)
    pivots = db.PIVOTS.find()

    targets = []
    targets.append({'name': 'スーパーマーケット', 'id': 1})
    targets.append({'name': 'コンビニエンスストア', 'id': 2})
    targets.append({'name': 'ラーメン', 'id': 3})
    targets.append({'name': '銭湯', 'id': 4})
    targets.append({'name': 'パン屋', 'id': 5})
    targets.append({'name': 'ドラッグストア', 'id': 8})
    targets.append({'name': '銀行', 'id': 9})
    targets.append({'name': '自動車学校', 'id': 10})

    for pivot in pivots:

        for target in targets:
            print(pivot['name'] + '周辺の' + target['name'] + 'の取得を開始')
            loc = [pivot['lat'], pivot['lng']]
            places = getPlacesAroundPivot(loc, target['name'])
            data = extractDataForMongo(places, target['id'])

            for d in data:
                try:
                    db.PLACE.insert_one(d)
                except Exception:
                    print(d['name'])
                    pass

            print()
        print()
    print()
    
if __name__ == "__main__":
    googleapikey = 'AIzaSyDxyk2TDT8NzAd4yp9YRawsp7ZJ-IfFDK4' # 後でどうにかして隠蔽する
    gmaps = googlemaps.Client(key=googleapikey)
    ku = getGeocodeOfPlace('京都大学')
    main()
