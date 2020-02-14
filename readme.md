## 環境構築
```
$ python3.6 -m pip install -r requirements.txt
```
pipを用いてパッケージをインストールするなら`requirements.txt`への追記は絶対！

## setup mongoDB
Dockerからパクってくるなら
```
$ docker pull mongo
$ docker run -d -p 27017:27017 --name evalhome mongo
```
で多分いける。

```
$ mogo evalhome
$ db.createCollection('PLACE')
$ show collections
```

## start server
```
$ python3.6 index.py &
```

