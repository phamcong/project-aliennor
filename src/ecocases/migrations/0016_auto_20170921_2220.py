# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-21 22:20
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('ecocases', '0015_esm_esm_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ecocase',
            name='ecocase_description',
            field=tinymce.models.HTMLField(),
        ),
    ]