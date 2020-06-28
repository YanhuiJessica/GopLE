from django.db import models
import mongoengine
from mongoengine.fields import EmbeddedDocumentField, ListField, StringField

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
    imdbId = mongoengine.IntField()
    tmdbId = mongoengine.IntField()
    tags = ListField(EmbeddedDocumentField('Tag'))
    meta = {'collection': 'Movies'}
