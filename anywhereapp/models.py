# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Song(models.Model):
	title = models.CharField(max_length=50)
	author = models.CharField(max_length=50, blank='true')
	verses = models.TextField(blank='true')
	prechorus = models.TextField(blank='true');
	chorus = models.TextField(blank='true');
	bridge = models.TextField(blank='true');
	additiomal_title = models.CharField(max_length=50, blank='true')