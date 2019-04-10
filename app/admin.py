from django.contrib import admin
from pedidos.models import comanda, adicional, sorvete, acai, itemacai, mix, itemmix, mshake, petit, fondue, suco, creme, produto, casadinho
from caixa.models import caixa_geral
from outros.models import senha

admin.site.register(comanda)
admin.site.register(adicional)
admin.site.register(acai)
admin.site.register(itemacai)
admin.site.register(caixa_geral)
admin.site.register(itemmix)
admin.site.register(mix)
admin.site.register(sorvete)
admin.site.register(mshake)
admin.site.register(petit)
admin.site.register(fondue)
admin.site.register(suco)
admin.site.register(creme)
admin.site.register(produto)
admin.site.register(casadinho)
admin.site.register(senha)