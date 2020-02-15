class Spot:

    SUPERMARKET = 1 # スーパー
    CONVINIENCESTOROE = 2 # コンビニ
    NOODLE = 3 # ラーメン
    SENTO = 4 # 銭湯
    BAKERY = 5 # パン屋
    KYOTOUNIV = 6 # 京大
    DAIMONJI = 7 # 大文字
    DRAGSTORE = 8 # ドラックストア
    BANK = 9 # 銀行
    CARSCHOOL = 10 # 車高

    def __init__(self, lat: float, lng: float, name: str, tag: int, review=0.0):
        self.lat = lat
        self.lng = lng
        self.name = name
        self.tag = tag
        self.review = review