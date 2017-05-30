from django.db import models

from Categories.models import Category

STATE_PRIVATE = 'BOR'
STATE_PUBLIC = 'PUB'

STATE = {
    (STATE_PUBLIC, 'Publicado'),
    (STATE_PRIVATE, 'Borrador')
}


class Post(models.Model):
    author = models.IntegerField(default=None)
    author_username = models.CharField(max_length=25, default=None)
    title = models.CharField(max_length=200)
    intro = models.TextField(max_length=1000)
    content = models.TextField()
    url_media = models.URLField()
    publicated_at = models.DateTimeField()
    state = models.CharField(max_length=3, choices=STATE, default=STATE_PUBLIC)
    category = models.ManyToManyField(Category)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)
