# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-02 17:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20171229_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(blank=True, default='users/avatar/default.png', max_length=200, null=True, upload_to='users/avatar/%Y/%m', verbose_name='用户头像'),
        ),
    ]
