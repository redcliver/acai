from django.contrib import admin
from pedidos.models import comanda, adicional, acai, itemacai
from caixa.models import caixa

admin.site.register(comanda)
admin.site.register(adicional)
admin.site.register(acai)
admin.site.register(itemacai)
admin.site.register(caixa)