from django.db import models
import datetime
# Create your models here.

import mongoengine
from mongoengine.fields import EmbeddedDocumentField, ListField, StringField

class watchedMovies(mongoengine.EmbeddedDocument):
    movieId = mongoengine.IntField()
    # 时间戳转日期显示 - 下面参考代码 - 按需获取
    # d = datetime.datetime.fromtimestamp(timeStamp)
    # str1 = d.strftime("%Y-%m-%d %H:%M:%S.%f")
    timestamp = mongoengine.IntField(max_length=50)
    rating = mongoengine.FloatField()

class Users(mongoengine.Document):
    userId = mongoengine.IntField()
    name = mongoengine.StringField(max_length=50)
    gender = mongoengine.StringField(max_length=3) 
    watchedMovies = ListField(EmbeddedDocumentField('watchedMovies'))
    meta = {'collection': 'user'}


# Create your models here.
class Tag(mongoengine.EmbeddedDocument):
    tag = mongoengine.StringField(max_length=255)
    tagId = mongoengine.IntField()
    relevance = mongoengine.FloatField()

class Movies(mongoengine.Document):
    movieId = mongoengine.IntField()
    title = mongoengine.StringField(max_length=255)
    year = mongoengine.IntField()
    genres = ListField(StringField(max_length=30))
    votes = mongoengine.IntField()
    rating = mongoengine.FloatField()
    favg = mongoengine.FloatField()
    mavg = mongoengine.FloatField()
    imdbId = mongoengine.IntField()
    tmdbId = mongoengine.IntField()
    tags = ListField(EmbeddedDocumentField('Tag'))
    meta = {'collection': 'Movies'}

