# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-01 16:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_comic_created_at'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Mobile',
        ),
    ]
