# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-07 17:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('author', models.CharField(blank='true', max_length=50)),
                ('verses', models.TextField(blank='true')),
                ('prechorus', models.TextField(blank='true')),
                ('chorus', models.TextField(blank='true')),
                ('bridge', models.TextField(blank='true')),
                ('additiomal_title', models.CharField(blank='true', max_length=50)),
            ],
        ),
    ]
