# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-24 10:36
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
            name='Areas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_code', models.CharField(max_length=64, unique=True, verbose_name='地区编码')),
                ('name', models.CharField(max_length=64, verbose_name='区名')),
            ],
            options={
                'db_table': 'areas',
            },
        ),
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_code', models.CharField(max_length=64, unique=True, verbose_name='市编码')),
                ('name', models.CharField(max_length=64, verbose_name='省份名')),
            ],
            options={
                'db_table': 'cities',
                'verbose_name_plural': '市',
            },
        ),
        migrations.CreateModel(
            name='FaultRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform', models.CharField(max_length=64, verbose_name='平台名称')),
                ('incident', models.CharField(max_length=128, verbose_name='故障事件')),
                ('start_time', models.DateTimeField(verbose_name='故障时间')),
                ('reason', models.TextField(verbose_name='故障原因')),
                ('handling_method', models.TextField(verbose_name='处理办法')),
                ('handling_time', models.DateTimeField(verbose_name='处理时间')),
                ('result', models.PositiveSmallIntegerField(choices=[(0, '已处理'), (1, '未处理'), (2, '暂无法处理')], default=0, verbose_name='处理结果')),
                ('ps', models.TextField(verbose_name='备注')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('area', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='record.Areas', verbose_name='区')),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='record.Cities', verbose_name='市')),
                ('handling_person', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='处理人')),
            ],
            options={
                'verbose_name_plural': '故障记录',
            },
        ),
        migrations.CreateModel(
            name='Provinces',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='省份名')),
                ('province_code', models.CharField(max_length=64, unique=True, verbose_name='省份编码')),
            ],
            options={
                'db_table': 'provinces',
                'verbose_name_plural': '省份',
            },
        ),
        migrations.CreateModel(
            name='RecordTags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='故障标签名')),
            ],
            options={
                'verbose_name_plural': '故障标签',
            },
        ),
        migrations.AddField(
            model_name='faultrecord',
            name='province',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='record.Provinces', verbose_name='省份'),
        ),
        migrations.AddField(
            model_name='cities',
            name='province',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='record.Provinces', verbose_name='所属省份'),
        ),
        migrations.AddField(
            model_name='areas',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='record.Cities', verbose_name='市名'),
        ),
        migrations.AlterUniqueTogether(
            name='cities',
            unique_together=set([('province', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='areas',
            unique_together=set([('city', 'name')]),
        ),
    ]