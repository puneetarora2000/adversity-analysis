
from django.contrib import admin

from django import forms
from django.contrib import admin
from django.forms.models import BaseInlineFormSet
import re

# Register your models here.
from .models import origin_country_attacker,InformationSource,OrganisedInformation,SpearIncidenceDetail,Subjects,attackaim,attackmethod,industry,topeleveldomain,The_Analysis,country_under_attack
# Register your models here.

class SubjectForm(forms.ModelForm):
    model = Subjects

class SubjectsAdmin(admin.ModelAdmin):
    search_fields = ['NameofSubject','LastUpdate']
    form = SubjectForm
    list_display = ('NameOfTheSubject', 'LastUpdate')
    list_per_page = 20

#----------------------------------------------
class informationsourceForm(forms.ModelForm):
    model = InformationSource

class InformationSourceAdmin(admin.ModelAdmin):
    search_fields = ['Name','LastUpdate']
    form = SubjectForm
    list_display = ('Name','ParentInformationSourceID' ,'LastUpdate')
    list_per_page = 25


#----------------------------------------------
class OrganisedInformationForm(forms.ModelForm):
    model = OrganisedInformation

class OrganisedInformationAdmin(admin.ModelAdmin):
    search_fields = ['SpearPhishingIncidencenumber','EntryDateofAddition','MoreInfor','LastUpdate']
    form = OrganisedInformationForm
    list_display = ('SpearPhishingIncidencenumber','EntryDateofAddition','MoreInfor','IncidenceDescription' ,'LastUpdate')
    list_per_page = 25



class Spear_Incidence_DetailForm(forms.ModelForm):
    model = SpearIncidenceDetail

class Spear_Incidence_DetailAdmin(admin.ModelAdmin):
    search_fields = ['SpearPhishingIncidencenumber','Spear_Attack_Method','Aim_Ofthe_Attack']
    form = Spear_Incidence_DetailForm
    list_display = ('SpearPhishingIncidencenumber','Attacktargetbrand','Attacktargetcountry','Attack_Top_Level_Domain','Spear_Attack_Method','Attacktargetindiviual','Content_As_Spear','Aim_Ofthe_Attack','Attackorigincountry','LastUpdate')
    list_per_page = 25


admin.site.register(InformationSource,InformationSourceAdmin)
admin.site.register(Subjects,SubjectsAdmin)
admin.site.register(SpearIncidenceDetail, Spear_Incidence_DetailAdmin)
admin.site.register(OrganisedInformation ,OrganisedInformationAdmin)
admin.site.register(industry)
admin.site.register(topeleveldomain)
admin.site.register(attackaim)
admin.site.register(attackmethod)
admin.site.register(origin_country_attacker)
admin.site.register(country_under_attack)
admin.site.register(The_Analysis)