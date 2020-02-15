import googlemaps
import time
from pymongo import MongoClient

def getGeocodeOfPlace(place_name):
    result = gmaps.geocode(place_name)
    geocode = result[0]['geometry']['location']

    return geocode

def getPlacesAroundKu(facility_name):
    tmp = gmaps.places_nearby(location=ku,
                              keyword=facility_name,
                              radius='5000',
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
                print('retry')

        places += tmp['results']

    return places

def extractDataForMongo(places, id):
    data = []
    for place in places:
        dic = {}
        dic['tag'] = id
        dic['name'] = place['name']
        dic['lat'] = place['geometry']['location']['lat']
        dic['lng'] = place['geometry']['location']['lng']
        dic['rating'] = place['rating']
        data.append(dic)

    return data


def main():
    target = {'name': 'スーパーマーケット', 'id': 1} #変更してね

    places = getPlacesAroundKu(target['name'])
    data = extractDataForMongo(places, target['id'])

    mongo = MongoClient('localhost', 27017)
    db=mongo['evalhome']

    db.PLACE.insert(data)


if __name__ == "__main__":
    googleapikey = 'AIzaSyDxyk2TDT8NzAd4yp9YRawsp7ZJ-IfFDK4' # 後でどうにかして隠蔽する
    gmaps = googlemaps.Client(key=googleapikey)
    ku = getGeocodeOfPlace('京都大学')
    main()
