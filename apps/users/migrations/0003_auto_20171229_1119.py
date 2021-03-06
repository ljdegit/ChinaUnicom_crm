# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-29 11:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20171227_1040'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='mobile',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='手机号码'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='qq',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='QQ号码'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='wechat',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='微信号码'),
        ),
    ]
