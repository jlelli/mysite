from django.db import models
from django.core.validators import URLValidator

class Page(models.Model):
    url = models.CharField(max_length=100, validators=[URLValidator])
    title = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    content_markdown = models.TextField('Content body', help_text='Use Markdown syntax.')
    content = models.TextField('Entry body as HTML', blank=True, null=True)
    last_modified = models.DateTimeField('last modified')

    def __unicode__(self):
        return self.title

    def save(self):
        import markdown
        self.content = markdown.markdown(self.content_markdown)
        super(Page, self).save()
