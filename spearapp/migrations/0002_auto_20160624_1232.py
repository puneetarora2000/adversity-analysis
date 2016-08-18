# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-24 07:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spearapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spearincidencedetail',
            name='Attacktopleveldomain',
        ),
        migrations.RemoveField(
            model_name='subjects',
            name='Name',
        ),
        migrations.AddField(
            model_name='spearincidencedetail',
            name='Attack_Top_Level_Domain',
            field=models.IntegerField(choices=[(1, 'AAA'), (2, 'AARP'), (3, 'ABB'), (4, 'COM'), (5, 'EDU'), (6, 'NET'), (7, 'IN'), (8, 'US'), (9, 'UK'), (10, 'INFO'), (11, 'CLUB'), (12, 'No Available')], default=1, verbose_name='Top Level Domain'),
        ),
        migrations.AddField(
            model_name='subjects',
            name='NameOfSubject',
            field=models.CharField(default='Spear Phishing', max_length=100),
        ),
        migrations.AlterField(
            model_name='spearincidencedetail',
            name='Aim_Ofthe_Attack',
            field=models.IntegerField(choices=[(1, 'Financial'), (2, 'Extortion'), (3, 'Corporate Espionage'), (4, 'Political-Espionage'), (5, 'Militarily-Espionage'), (6, 'Militarily-Espionage'), (7, 'Insider-Attacker-Sabotage'), (8, 'Business-Continuity-Disruption'), (9, 'Compromise-Data-Integrity'), (10, 'Data-Leakage'), (11, 'Other-Unknown-Motive'), (12, 'Cyber-Terrorism'), (13, 'Cyber-Bulling-Trolling'), (14, 'Not Available')], default=1, verbose_name='Aim of the Spear Phishing Attack'),
        ),
        migrations.AlterField(
            model_name='spearincidencedetail',
            name='Attackduration',
            field=models.FloatField(max_length=12, verbose_name='Attack Duration'),
        ),
        migrations.AlterField(
            model_name='spearincidencedetail',
            name='Attackoriginip',
            field=models.IntegerField(verbose_name='Attack_Origininating IP Address '),
        ),
        migrations.AlterField(
            model_name='spearincidencedetail',
            name='Attacktargetbrand',
            field=models.CharField(max_length=222, verbose_name='Attack_Target_Brand_Name'),
        ),
        migrations.AlterField(
            model_name='spearincidencedetail',
            name='Attacktargetindustry',
            field=models.IntegerField(choices=[(1, 'Banking'), (2, 'Financial'), (3, 'Petroleum'), (4, 'Energy'), (5, 'Celebrity'), (6, 'Govt'), (7, 'Political Party'), (8, 'Construction'), (9, 'Computer'), (10, 'Agriculture'), (11, 'Pharma'), (12, 'Health'), (13, 'Telcom'), (14, 'Water'), (15, 'MassMedia'), (16, 'Food'), (17, 'Rail'), (18, 'Transport'), (19, 'No Available')], verbose_name='Which Industry'),
        ),
        migrations.AlterField(
            model_name='spearincidencedetail',
            name='SpearPhishingIncidencenumber',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='spearapp.Organised_Information'),
        ),
        migrations.AlterField(
            model_name='spearincidencedetail',
            name='Spear_Attack_Type',
            field=models.IntegerField(choices=[(1, 'Email'), (2, 'Misleading-Advertisement'), (3, 'Misleading-Office-Memo'), (4, 'Misleading-Information'), (5, 'Email-With-Attachment'), (6, 'PDF-As-Attachment'), (7, 'Email-With-DLL'), (8, 'Adobe-Flash-Player'), (9, 'Torjan'), (10, 'Clone-Site-Link'), (11, 'Social-Media-Request-Message'), (12, 'Not Available')], default=1, verbose_name='Attack Type'),
        ),
    ]
