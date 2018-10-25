from django.conf.urls import include, url
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name='blog' 

urlpatterns = [
    url(r'^$', views.home, name='home'),
    
    url(r'^Usuario_List', views.usuario_list, name='usuario_list'),
    url(r'^Registro', views.registro, name='registro'),
    url(r'^usuario/(?P<pk>[0-9]+)/$', views.usuario_detail, name='usuario_detail'),
    url(r'^usuario/(?P<pk>[0-9]+)/edit/$', views.usuario_edit, name='usuario_edit'), 
    url(r'^Mascota_List/$',views.mascota_list),
]

urlpatterns += staticfiles_urlpatterns()
