# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-23 21:37
from __future__ import unicode_literals

import books.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0014_auto_20160520_1738'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='external_link',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=books.models.author_upload_location),
        ),
    ]
