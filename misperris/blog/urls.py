from django.conf.urls import include, url
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name='blog' 

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^Mascota_List',views.mascota_list,name='mascota_list'),
    url(r'^Usuario_List', views.usuario_list, name='usuario_list'),
    url(r'^mascota/(?P<pk>[0-9]+)/$', views.mascota_detail, name='mascota_detail'),
    url(r'^mascota/(?P<pk>[0-9]+)/edit/$', views.mascota_edit, name='mascota_edit'),
    url(r'^Registro', views.registro, name='registro'),
    path('ajax/load-cities/', views.load_ciudades, name='load_ciudades'),
    url(r'^usuario/(?P<pk>[0-9]+)/$', views.usuario_detail, name='usuario_detail'),
    url(r'^usuario/(?P<pk>[0-9]+)/edit/$', views.usuario_edit, name='usuario_edit'), 
    url(r'^mascota/new/$', views.mascota_new, name='mascota_new'),
]

urlpatterns += staticfiles_urlpatterns()
