
from django.conf.urls import url
from . import views
from django.contrib.auth.views import login


urlpatterns = [
    url(r'^$', views.pedidos),
    url(r'^confirmacao/$', views.confirmacao),
    url(r'^tamanho/$', views.tamanho),
    url(r'^adicionais/$', views.adicionais),
    url(r'^finalizar/$', views.finalizar),
    url(r'^metodo/$', views.metodo),
    url(r'^dinheiro/$', views.dinheiro),
    url(r'^cartao/$', views.cartao),
    url(r'^troco/$', views.troco),
    ]
