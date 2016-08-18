from django.conf.urls import url

from . import views

app_name = 'spearapp'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^subjects/$', views.subjects, name='subjects'),
    url(r'^informationsources/$', views.informationsources, name='informationsources'),
    url(r'^details/$', views.details, name='details'),
    url(r'^statistics/$', views.statistics, name='statistics'),
    url(r'^attackaimstatistics/$',views.attackaimstatistics,name='attackaimstatistics'),
    url(r'^organisedinformation/$',views.organisedinformation,name='organisedinformation'),
     url(r'^attackdetails/$',views.attackdetails,name='attackdetails'),
    url(r'^test/$',views.test,name='test'),

]