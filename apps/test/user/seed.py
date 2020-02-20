from apps.models.user import User
from apps import wave, mongo

def evalUser(user):
    total = wave.evaluate(user.lat, user.lng)
    user.setPoint(total)

def createSampleUser(n=10):
    rge_lng = [135.776338, 135.789470]
    rge_lat = [35.025129, 35.038693]
    users = []

    lng_max = n
    lat_max = n
    rge_lng.append((rge_lng[1]-rge_lng[0])/lng_max)
    rge_lat.append((rge_lat[1]-rge_lat[0])/lat_max)
    for lng_num in range(lng_max):
        for lat_num in range(lat_max):
            user = User(rge_lat[2]*lat_num + rge_lat[0],rge_lng[2]*lng_num + rge_lng[0])
            users.append(user)
    return users

def seedUser():
    users = createSampleUser()
    dummped = []
    for u in users:
        evalUser(u)
        dummped.append(u.dump())