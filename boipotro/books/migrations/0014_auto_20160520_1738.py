# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-20 17:38
from __future__ import unicode_literals

import books.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0013_auto_20160520_1355'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_file',
            field=models.FileField(default=True, upload_to=books.models.upload_location),
            preserve_default=False,
        ),
    ]
