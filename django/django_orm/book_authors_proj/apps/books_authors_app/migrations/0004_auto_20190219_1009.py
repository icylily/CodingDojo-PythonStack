# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-02-19 18:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0003_auto_20190219_0542'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Authors',
            new_name='Author',
        ),
        migrations.RenameModel(
            old_name='Books',
            new_name='Book',
        ),
    ]
