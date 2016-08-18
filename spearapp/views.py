from __future__ import unicode_literals, division
from django.shortcuts import render
from models import AttackAim,Industry_Choices,Spear_Attack_Type
import pandas as pd
import stats
import ujson
from django.db.models import Count
# Create your views here
from django.http import Http404
from django.shortcuts import render
#from datetime import datetime

#from django.http import HttpResponse
from django.template import loader
from .models import Subjects,OrganisedInformation,InformationSource,SpearIncidenceDetail,country_under_attack,origin_country_attacker,topeleveldomain,attackmethod,attackaim
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

#from django.views.generic import ListView

#import re
#from pandas import *
#import string
#from django.db.models import Count
#from scipy import spatial
#import numpy as np

#import random
#from operator import itemgetter


def index(request):
    return render(request, 'spearapp/index.html', {})

def subjects(request):
    Subjects_list = Subjects.objects.order_by('-LastUpdate')
    paginator = Paginator(Subjects_list, 20) # Show 20 items per page
    page = request.GET.get('page')
    try:
        Subjectss = paginator.page(page)
    except PageNotAnInteger:
         #If page is not an integer, deliver first page.
        Subjectss = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        Subjectss = paginator.page(paginator.num_pages)
    return render(request,  'spearapp/subjects.html', {'gui_sujects': Subjectss, 'callout_list':['success','warning','danger','info']})


def informationsources(request):
    InformationSource_list = InformationSource.objects.order_by('-LastUpdate')
    paginator = Paginator(InformationSource_list, 20) # Show 20 items per page

    page = request.GET.get('page')
    try:
        InformationSources = paginator.page(page)
    except PageNotAnInteger:
         #If page is not an integer, deliver first page.
        InformationSources = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        InformationSources = paginator.page(paginator.num_pages)
    return render(request,  'spearapp/informationsources.html', {'gui_values': InformationSources, 'callout_list':['success','warning','danger','info']})

def attackdetails(request):
    Spear_Incidence_Detail_list = SpearIncidenceDetail.objects.order_by('-LastUpdate')
    paginator = Paginator(Spear_Incidence_Detail_list, 5) # Show 20 items per page

    page = request.GET.get('page')
    try:
        Spear_Incidence_Details = paginator.page(page)
    except PageNotAnInteger:
         #If page is not an integer, deliver first page.
        Spear_Incidence_Details = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        Spear_Incidence_Details = paginator.page(paginator.num_pages)
    return render(request,  'spearapp/SpearIncidenceDetail.html', {'gui_values': Spear_Incidence_Details, 'callout_list':['success','warning','danger','info']})

def organisedinformation(request):
    InformationSource_list = OrganisedInformation.objects.order_by('-LastUpdate')
    paginator = Paginator(InformationSource_list, 20) # Show 20 items per page

    page = request.GET.get('page')
    try:
        Organised_Informations = paginator.page(page)
    except PageNotAnInteger:
         #If page is not an integer, deliver first page.
        Organised_Informations = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        Organised_Informations = paginator.page(paginator.num_pages)
    return render(request,  'spearapp/Organised_Information.html', {'gui_values': Organised_Informations, 'callout_list':['success','warning','danger','info']})

def details(request):
    subjects = Subjects.objects.all()
    informationsources = InformationSource.objects.all()
    organisedinformations = OrganisedInformation.objects.all()

    return render(request, 'spearapp/details.html', {'subjects': subjects, 'informationsources': informationsources, 'organisedinformations': organisedinformations})
def statistics(request):
    #spear_incidence_df = pd.DataFrame.from_records(SpearIncidenceDetail.objects.all().values('Attack_Top_Level_Domain', 'Attackduration', 'Attackorigincountry', 'Attackoriginip', 'Attacktargetbrand', 'Attacktargetcountry', 'Attacktargetindiviual', 'Attacktargetindustry'))
    spear_incidence_df = pd.DataFrame.from_records(SpearIncidenceDetail.objects.all().values('Attackorigincountry'))
    incidence_stats = stats.collect_stats(spear_incidence_df, spear_incidence_df.columns.values)
    # print spear_incidence_df.columns.values
    return render(request, 'spearapp/stats.html', {'incidence_stats': incidence_stats})

def attackaimstatistics(request):
    df = pd.DataFrame.from_records(SpearIncidenceDetail.objects.all().values('Attackorigincountry_id'))
    grouped = df.groupby('Attackorigincountry_id',sort=True)
    table = grouped
    return render(request, 'spearapp/stats.html', {'incidence_stats': table, 'values': grouped})
    #return render_template("analysis.html", name=filename, data=x.to_html())


 # AimsIDs  = attackaim.objects.all().values('id')
    # AimsNames  = attackaim.objects.all().values('AttackAim')
    # table = []
    # for x in AimsIDs:
    #     for t in AimsIDs[x]:
    #         allobjects = SpearIncidenceDetail.objects.filter(Spear_Attack_Method__in=t).prefetch_related()
    #         count = len(allobjects)

def test(request):

    incidence_stats = SpearIncidenceDetail.objects.all().values('Spear_Attack_Method__AttackMethod').annotate(attackcount=Count('Spear_Attack_Method'))
    Attackorigincountry_stats = SpearIncidenceDetail.objects.all().values('Attackorigincountry__Origin_Country_Attacker').annotate(attackcount=Count('Attackorigincountry'))
    Attacktargetindustry_stats = SpearIncidenceDetail.objects.all().values('Attacktargetindustry__Industry_Name').annotate(attackcount=Count('Attacktargetindustry'))
    Aim_Ofthe_Attack_stats = SpearIncidenceDetail.objects.all().values('Aim_Ofthe_Attack__AttackAim').annotate(attackcount=Count('Aim_Ofthe_Attack'))
    Attack_Top_Level_Domain_stats = SpearIncidenceDetail.objects.all().values('Attack_Top_Level_Domain__TopeLevelDomain_Name').annotate(attackcount=Count('Attack_Top_Level_Domain'))
    Attacktargetcountry_stats = SpearIncidenceDetail.objects.all().values('Attacktargetcountry__Country_Under_Attack').annotate(attackcount=Count('Attacktargetcountry'))
    Attacktargetbrand_stats = SpearIncidenceDetail.objects.all().values('Attacktargetbrand').annotate(attackcount=Count('Attacktargetbrand'))


    print Attacktargetbrand_stats
    return render(request, 'spearapp/stats.html', {'Attacktargetbrand_stats': ujson.dumps(Attacktargetbrand_stats),'Aim_Ofthe_Attack_stats': ujson.dumps(Aim_Ofthe_Attack_stats),'Attacktargetindustry_stats': ujson.dumps(Attacktargetindustry_stats),'Attack_Top_Level_Domain_stats': ujson.dumps(Attack_Top_Level_Domain_stats),'incidence_stats': ujson.dumps(incidence_stats),'Attackorigincountry_stats': ujson.dumps(Attackorigincountry_stats),'Attacktargetcountry_stats': ujson.dumps(Attacktargetcountry_stats) })

