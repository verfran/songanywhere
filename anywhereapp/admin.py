# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Song

class SongAdmin(admin.ModelAdmin):
	list_display = ('title','author')
	list_filter = ('title',)
	search_fields = ('title',)

admin.site.register(Song, SongAdmin)
