
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.pedidos),
    url(r'^novo_pedido/$', views.novo_pedido),
    url(r'^entrega/$', views.entrega),
    url(r'^local/$', views.local),
    url(r'^viagem/$', views.viagem),
    url(r'^confirmacao/$', views.confirmacao),
    url(r'^tamanho/$', views.tamanho),
    url(r'^adicionais/$', views.adicionais),
    url(r'^finalizar/$', views.finalizar),
    url(r'^excluir/$', views.excluir),
    url(r'^finalizar1/$', views.finalizar1),
    url(r'^finalizar2/$', views.finalizar2),
    url(r'^metodo/$', views.metodo),
    url(r'^dinheiro/$', views.dinheiro),
    url(r'^cartao/$', views.cartao),
    url(r'^troco/$', views.troco),
    url(r'^desconto/$', views.desconto),
    ]
