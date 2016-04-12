# trips/models.py

from django.db import models
from elasticsearch_dsl import DocType, String


class PostDoc(DocType):
    title = String()
    content = String()

    class Meta:
        index = 'trip_post'


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    photo = models.URLField(blank=True)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def sync_to_es(self):
        PostDoc.init()
        doc = PostDoc(
            title=self.title, content=self.content
        )
        doc.meta.id = self.id
        doc.save()
