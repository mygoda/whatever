# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-28 09:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MemberFans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_valid', models.BooleanField(default=True, verbose_name='是否有效')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ZhihuMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=128, verbose_name='姓名')),
                ('gender', models.CharField(choices=[('1', '男'), ('-1', '女')], default='1', max_length=2, verbose_name='性别')),
                ('user_type', models.CharField(blank=True, max_length=16, null=True, verbose_name='用户类型')),
                ('url_token', models.CharField(max_length=32, unique=True, verbose_name='用户URL')),
                ('is_advertiser', models.BooleanField(default=False, verbose_name='是否广告')),
                ('avatar_url', models.CharField(max_length=255, verbose_name='头像')),
                ('is_org', models.BooleanField(default=False, verbose_name='是否组织')),
                ('type', models.CharField(blank=True, max_length=32, null=True, verbose_name='类型')),
                ('zhihu_id', models.CharField(max_length=36, unique=True, verbose_name='知乎ID')),
                ('headline', models.CharField(blank=True, max_length=128, null=True, verbose_name='headline')),
                ('w_count', models.IntegerField(default=1, verbose_name='关注了')),
                ('f_count', models.IntegerField(default=1, verbose_name='关注者')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='memberfans',
            name='fans',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fans', to='zhihu.ZhihuMember', verbose_name=' 关注者'),
        ),
        migrations.AddField(
            model_name='memberfans',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='member', to='zhihu.ZhihuMember', verbose_name='被关注'),
        ),
    ]
