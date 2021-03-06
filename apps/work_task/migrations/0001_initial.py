# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-03 18:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserWorkTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_level', models.PositiveSmallIntegerField(choices=[(1, '紧急'), (2, '一般'), (3, '不急')], default=2, verbose_name='紧急程度')),
                ('content', models.TextField(verbose_name='任务内容')),
                ('start_time', models.DateTimeField(verbose_name='开始时间')),
                ('stop_time', models.DateTimeField(verbose_name='截止时间')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, '已完成'), (1, '进行中'), (2, '延期中 '), (3, '已终止')], default=1, verbose_name='任务状态')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('ps', models.TextField(blank=True, null=True, verbose_name='备注')),
                ('create_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='c_user', to=settings.AUTH_USER_MODEL, verbose_name='发起者')),
                ('send_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='s_user', to=settings.AUTH_USER_MODEL, verbose_name='指派者')),
            ],
            options={
                'verbose_name': '任务表',
                'verbose_name_plural': '任务表',
            },
        ),
    ]
