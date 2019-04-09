from django.contrib import admin
from .models import Blog_news, Categories
from tinymce.widgets import TinyMCE
from django.db import models

class Blog_newsAdmin(admin.ModelAdmin):
	fieldsets=[("Title and Date",
		        {"fields": ['date', 'tittle']}),
				("Category", {"fields":["news_category"]}),
		       ("Content",
		       	{"fields":['image','text', 'published_date']}),
	           ]
	formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        }
	

# Register your models here.
admin.site.register(Categories)
admin.site.register(Blog_news, Blog_newsAdmin)
