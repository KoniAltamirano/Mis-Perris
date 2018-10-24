from django.conf.urls import include, url
from . import views

app_name='blog' 

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^Inicio', views.home_register, name='home_register'),
    url(r'^Usuario_List', views.usuario_list, name='usuario_list'),
    url(r'^Registro', views.registro, name='registro'),
    url(r'^usuario/(?P<pk>[0-9]+)/$', views.usuario_detail, name='usuario_detail'),
    url(r'^usuario/(?P<pk>[0-9]+)/edit/$', views.usuario_edit, name='usuario_edit'), 
]
