from django.contrib import admin
from . import models

# Register your models here.


admin.site.register(models.BlogAuthor)
admin.site.register(models.Comment)


class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'author']

    class Meta:
        model = models.Blog


admin.site.register(models.Blog, BlogAdmin)
