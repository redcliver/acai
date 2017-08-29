from django.contrib import admin
from pedidos.models import comanda, adicional, sorvete, acai, itemacai, mix, itemmix
from caixa.models import caixa

admin.site.register(comanda)
admin.site.register(adicional)
admin.site.register(acai)
admin.site.register(itemacai)
admin.site.register(caixa)
admin.site.register(itemmix)
admin.site.register(mix)
admin.site.register(sorvete)