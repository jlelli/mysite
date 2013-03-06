from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import Context, loader

from flatpage.models import Page

def index(request, url):
    template = loader.get_template('flatpage/index.html')
    page = get_object_or_404(Page, url=url)

    return render(request, 'flatpage/index.html',
        {'title': page.title,
         'image': page.image,
         'content': page.content,
         'last_modified': page.last_modified})
