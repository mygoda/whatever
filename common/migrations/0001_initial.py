# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-28 06:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ZhihuAuthorization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=255, verbose_name='值')),
            ],
        ),
        migrations.CreateModel(
            name='ZhihuStartMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_token', models.CharField(max_length=255, verbose_name='url')),
                ('is_valid', models.BooleanField(default=True, verbose_name='是否有效')),
            ],
        ),
    ]
