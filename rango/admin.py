from django.contrib import admin
from rango import models


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

admin.site.register(models.Category)
admin.site.register(models.Page, PageAdmin)
