# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-20 00:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecocases', '0002_auto_20170917_2144'),
    ]

    operations = [
        migrations.AddField(
            model_name='ecocase',
            name='ecocase_images',
            field=models.FileField(null=True, upload_to='ecocases/'),
        ),
        migrations.AddField(
            model_name='ecocase',
            name='img_url_list',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AlterField(
            model_name='ecocase',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]