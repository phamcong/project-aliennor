# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-20 10:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecocases', '0006_auto_20170920_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ecocase',
            name='ecocase_images',
            field=models.FileField(null=True, upload_to='ecocases'),
        ),
    ]