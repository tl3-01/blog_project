from django.contrib import admin

from .models import BlogPost, Content

# Register your models here.
admin.site.register(BlogPost)
admin.site.register(Content)
