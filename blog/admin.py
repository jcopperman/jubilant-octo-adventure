from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Blog

class BlogAdmin(SummernoteModelAdmin):
    #list_display = ('title', 'body', 'pub_date')
    #search_fields = ['title', 'pub_date']
    summernote_fields = ('body',)


admin.site.register(Blog, BlogAdmin)
