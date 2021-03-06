# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-02-05 23:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('School', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='teachers',
            field=models.ManyToManyField(blank=True, related_name='teachers', to='School.Teacher'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='students',
            field=models.ManyToManyField(blank=True, related_name='students', to='School.Student'),
        ),
    ]
