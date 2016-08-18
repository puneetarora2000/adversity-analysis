# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-27 11:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spearapp', '0015_auto_20160627_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spearincidencedetail',
            name='Attackduration',
            field=models.FloatField(default=1, max_length=12, verbose_name='Attack Duration in Hours'),
        ),
        migrations.AlterField(
            model_name='spearincidencedetail',
            name='Attacktargetindiviual',
            field=models.CharField(default='Not Known', max_length=222, verbose_name='Attack_Target_Individual'),
        ),
    ]