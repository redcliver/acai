
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^novo_cliente/$', views.novo_cliente),
    ]
