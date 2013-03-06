from django.db import models
from django.core.validators import URLValidator

class Page(models.Model):
    url = models.CharField(max_length=100, validators=[URLValidator])
    title = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    content = models.TextField()
    last_modified = models.DateTimeField('last modified')
    def __unicode__(self):
        return self.title
