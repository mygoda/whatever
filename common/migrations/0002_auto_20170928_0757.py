# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-28 07:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='zhihuauthorization',
            name='UDID',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='UUID'),
        ),
        migrations.AddField(
            model_name='zhihuauthorization',
            name='agent',
            field=models.TextField(blank=True, default='', null=True, verbose_name='浏览器代理'),
        ),
    ]
