
from django.conf.urls import url
from . import views
from django.contrib.auth.views import login


urlpatterns = [
    url(r'^$', views.outros),
    url(r'^addadicional/$', views.addadicional),
    url(r'^addacai/$', views.addacai),
    url(r'^addcasadinho/$', views.addcasadinho),
    url(r'^addmix/$', views.addmix),
    url(r'^addcreme/$', views.addcreme),
    url(r'^addsorvete/$', views.addsorvete),
    url(r'^addproduto/$', views.addproduto),
    ]
