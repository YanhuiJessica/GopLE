from django.db import models
import datetime
# Create your models here.

import mongoengine
from mongoengine.fields import EmbeddedDocumentField, ListField, StringField

class watchedMovie(mongoengine.EmbeddedDocument):
    movieId = mongoengine.IntField()
    # 时间戳转日期显示 - 下面参考代码 - 按需获取
    # d = datetime.datetime.fromtimestamp(timeStamp)
    # str1 = d.strftime("%Y-%m-%d %H:%M:%S.%f")
    timestamp = mongoengine.IntField(max_length=50)
    rating = mongoengine.FloatField()

class user(mongoengine.Document):
    userId = mongoengine.IntField()
    name = mongoengine.StringField(max_length=50)
    gender = mongoengine.StringField(max_length=3) 
    watchedMovies = ListField(EmbeddedDocumentField('watchedMovie'))
