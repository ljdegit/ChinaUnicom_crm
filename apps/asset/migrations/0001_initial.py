# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-06 11:14
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
            name='IDC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='机房名称')),
                ('address', models.CharField(blank=True, max_length=128, null=True, verbose_name='机房地址')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '机房表',
                'verbose_name_plural': '机房表',
            },
        ),
        migrations.CreateModel(
            name='ServerInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_addr', models.GenericIPAddressField(verbose_name='IP地址')),
                ('server_name', models.CharField(max_length=64, verbose_name='主机名')),
                ('pro_name', models.CharField(max_length=64, verbose_name='项目名')),
                ('service_name', models.CharField(max_length=64, verbose_name='服务名称')),
                ('status', models.SmallIntegerField(choices=[(0, '关机'), (1, '开机'), (2, '其它')], verbose_name='主机状态')),
                ('ask_user', models.CharField(max_length=64, verbose_name='申请人')),
                ('user_name', models.CharField(max_length=32, verbose_name='登录用户名')),
                ('pass_word', models.CharField(max_length=64, verbose_name='登录密码')),
                ('ps', models.TextField(blank=True, null=True, verbose_name='备注')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('add_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='添加者')),
                ('idc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asset.IDC', verbose_name='机房')),
            ],
            options={
                'verbose_name': '服务器详情表',
                'verbose_name_plural': '服务器详情表',
            },
        ),
        migrations.CreateModel(
            name='System',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='系统名称')),
                ('byte', models.SmallIntegerField(default=64, verbose_name='位数')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '操作系统表',
                'verbose_name_plural': '操作系统表',
            },
        ),
        migrations.AlterUniqueTogether(
            name='system',
            unique_together=set([('name', 'byte')]),
        ),
        migrations.AddField(
            model_name='serverinfo',
            name='system',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asset.System', verbose_name='操作系统'),
        ),
        migrations.AlterUniqueTogether(
            name='serverinfo',
            unique_together=set([('ip_addr', 'idc')]),
        ),
    ]
