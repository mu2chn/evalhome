# Spotを検索する円の中心点となるような点の座標をdbに格納するためのスクリプト
import googlemaps
import time
from pymongo import MongoClient

def setDataOfPivot(place_name):
    result = gmaps.geocode(place_name)

    dic = {}
    dic['id'] = result[0]['place_id']
    dic['name'] = place_name
    dic['lat'] = result[0]['geometry']['location']["lat"]
    dic['lng'] = result[0]['geometry']['location']["lng"]

    db.PIVOTS.insert(dic)

googleapikey = 'AIzaSyDxyk2TDT8NzAd4yp9YRawsp7ZJ-IfFDK4' # 後でどうにかして隠蔽する
gmaps = googlemaps.Client(key=googleapikey)

targets = ['京都大学', '哲学の道', '南禅寺', '平安神宮', '三条駅', '出町柳駅', '一乗寺駅',
            '修学院駅', '北大路ビブレ', '京都造形芸術大学']

mongo = MongoClient('localhost', 27017)
db=mongo['evalhome']
for target in targets:
    setDataOfPivot(target)
