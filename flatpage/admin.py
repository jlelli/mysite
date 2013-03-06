from django.contrib import admin

from flatpage.models import Page

class PageAdmin(admin.ModelAdmin):
    change_form_template = 'admin/flatpage/page/change_form.html'
    fieldset = [
        (None,               {'fields': ['title']}),
        (None,               {'fields': ['image']}),
        (None,               {'fields': ['content_markdown']}),
        ('Date information', {'fields': ['last_modified']}),
    ]

admin.site.register(Page, PageAdmin)
