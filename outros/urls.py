
from django.conf.urls import url
from . import views
from django.contrib.auth.views import login


urlpatterns = [
    url(r'^$', views.outros),
    url(r'^addadicional/$', views.addadicional),
    url(r'^addacai/$', views.addacai),
    url(r'^addmix/$', views.addmix),
    ]
