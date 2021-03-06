# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-06 21:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('message', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cmt_content', models.TextField(verbose_name='消息')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='发送时间')),
                ('send_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='发送者')),
            ],
            options={
                'verbose_name': '用户评论',
                'verbose_name_plural': '用户评论',
            },
        ),
        migrations.CreateModel(
            name='UserMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('send_to', models.IntegerField(verbose_name='接收者')),
                ('msg_content', models.TextField(verbose_name='消息')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='评论时间')),
                ('send_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='发送者')),
            ],
            options={
                'verbose_name': '用户消息',
                'verbose_name_plural': '用户消息',
            },
        ),
        migrations.CreateModel(
            name='UserReadMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_read', models.BooleanField(default=False, verbose_name='是否读取')),
                ('add_time', models.DateTimeField(auto_now=True, verbose_name='读取时间')),
                ('msg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='message.UserMessage', verbose_name='消息')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '读取消息',
                'verbose_name_plural': '读取消息',
            },
        ),
        migrations.AddField(
            model_name='usercomment',
            name='user_msg',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='message.UserMessage', verbose_name='用户消息'),
        ),
    ]
