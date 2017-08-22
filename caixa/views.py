from django.shortcuts import render
from caixa.models import caixa
import datetime
from decimal import *

# Create your views here.
def caixa1(request):
    caixa_atual = caixa.objects.latest('id')
    return render(request, 'caixa.html', {'title':'Caixa', 'caixa_atual':caixa_atual})


def extrato(request):
    hoje = datetime.date.today()
    caixas = caixa.objects.filter(data__contains=hoje)
    return render(request, 'extrato.html', {'title':'Extrato', 'caixas':caixas})

def retirada(request):
    caixa_atual = caixa.objects.latest('id')
    if request.method == 'POST' and request.POST.get('retirada') != None:
        nova_retirada = request.POST.get('retirada')
        motivo = request.POST.get('motivo')
        caixa_atual = caixa.objects.latest('id')
        retirada_caixa = caixa_atual.total - Decimal(nova_retirada)
        retirada_item = "Retirada no valor de : "+ str(nova_retirada)
        novo_caixa = caixa(tipo="Saida", total=retirada_caixa, item=retirada_item, obs=motivo)
        novo_caixa.save()
        caixa_atual = caixa.objects.latest('id')
        return render(request, 'caixa.html', {'title':'Caixa', 'caixa_atual':caixa_atual})
    return render(request, 'retirada.html', {'title':'Retirada', 'caixa_atual':caixa_atual})