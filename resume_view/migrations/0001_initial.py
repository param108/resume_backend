# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-11-22 08:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import resume_view.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=300)),
                ('seq', models.IntegerField()),
                ('image', models.FileField(upload_to=resume_view.models.pic_directory_path)),
                ('caption', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=4)),
                ('title', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=50)),
                ('teamsize', models.IntegerField()),
                ('company', models.CharField(max_length=50)),
                ('desc', models.TextField()),
                ('pics_available', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Tech',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tech', models.CharField(max_length=20)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume_view.Project')),
            ],
        ),
        migrations.AddField(
            model_name='pics',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume_view.Project'),
        ),
    ]