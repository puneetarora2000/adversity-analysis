# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-24 16:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spearapp', '0009_auto_20160624_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spearincidencedetail',
            name='Attackorigincountry',
            field=models.CharField(default='Not Known', max_length=222, verbose_name='Attack_Origin_Country'),
        ),
        migrations.AlterField(
            model_name='spearincidencedetail',
            name='Attacktargetbrand',
            field=models.CharField(default='Not Known', max_length=222, verbose_name='AttackTargetBrand/Company'),
        ),
        migrations.AlterField(
            model_name='spearincidencedetail',
            name='Attacktargetcountry',
            field=models.CharField(default='Not Known', max_length=222, verbose_name='Attack_Target_Country'),
        ),
        migrations.AlterField(
            model_name='spearincidencedetail',
            name='Attacktargetindiviual',
            field=models.CharField(default='Not Known', max_length=222, verbose_name='Attack_Target_Indivi'),
        ),
        migrations.AlterField(
            model_name='spearincidencedetail',
            name='Attacktargetindustry',
            field=models.IntegerField(choices=[(1, 'Banking'), (2, 'Financial'), (3, 'Petroleum'), (4, 'Energy'), (5, 'Celebrity'), (6, 'Govt'), (7, 'Political Party'), (8, 'Construction'), (9, 'Computer'), (10, 'Agriculture'), (11, 'Pharma'), (12, 'Health'), (13, 'Telcom'), (14, 'Water'), (15, 'MassMedia'), (16, 'Food'), (17, 'Rail'), (18, 'Transport'), (19, 'No Available')], default='Not Known', verbose_name='Which Industry'),
        ),
    ]
