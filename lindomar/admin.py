from django.contrib import admin

from .models import *

class datSpell (admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', )
    search_fields = ('name',)
    list_per_page = 10

admin.site.register(Spell, datSpell)

class datChar (admin.ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('id',)
    list_per_page = 10

admin.site.register(Charcaters, datChar)

class datHouse (admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', )
    search_fields = ('name',)
    list_per_page = 10

admin.site.register(House, datHouse)