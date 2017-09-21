# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-20 15:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ecocases', '0008_auto_20170920_1737'),
    ]

    operations = [
        migrations.AddField(
            model_name='ecocase',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]