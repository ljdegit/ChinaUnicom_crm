# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-08 08:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0006_portmap'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portmap',
            name='start_time',
            field=models.DateField(verbose_name='开始时间'),
        ),
        migrations.AlterField(
            model_name='portmap',
            name='stop_time',
            field=models.DateField(verbose_name='结束时间'),
        ),
    ]
