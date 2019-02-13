from django.shortcuts import render
from caixa.models import caixa
from pedidos.models import comanda, itemproduto
import datetime
from decimal import *
from django.utils import timezone

# Create your views here.
def caixa1(request):
    caixa_atual = caixa.objects.latest('id')
    return render(request, 'caixa.html', {'title':'Caixa', 'caixa_atual':caixa_atual})


def extrato(request):
    hoje = datetime.date.today().strftime('%Y-%m-%d')
    caixas = caixa.objects.filter(data__contains=hoje)
    if request.method == 'POST':
        data1 = request.POST.get('data')
        caixas = caixa.objects.filter(data__icontains=data1)
        return render(request, 'extrato.html', {'title':'Extrato', 'caixas':caixas, 'hoje':data1})    
    return render(request, 'extrato.html', {'title':'Extrato', 'caixas':caixas, 'hoje':hoje})

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
        msg = "Retirada realizada com sucesso!"
        return render(request, 'home/home.html', {'title':'Home', 'msg':msg})
    return render(request, 'retirada.html', {'title':'Retirada', 'caixa_atual':caixa_atual})

def entrada(request):
    caixa_atual = caixa.objects.latest('id')
    if request.method == 'POST' and request.POST.get('entrada') != None:
        nova_retirada = request.POST.get('entrada')
        motivo = request.POST.get('motivo')
        caixa_atual = caixa.objects.latest('id')
        retirada_caixa = caixa_atual.total + Decimal(nova_retirada)
        retirada_item = "Entrada no valor de : "+ str(nova_retirada)
        novo_caixa = caixa(tipo="Entrada", total=retirada_caixa, item=retirada_item, obs=motivo)
        novo_caixa.save()
        caixa_atual = caixa.objects.latest('id')
        msg = "Entrada realizada com sucesso!"
        return render(request, 'home/home.html', {'title':'Home', 'msg':msg})
    return render(request, 'entrada.html', {'title':'Retirada', 'caixa_atual':caixa_atual})

def fechar(request):
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
        msg = "Retirada realizada com sucesso!"
        return render(request, 'home/home.html', {'title':'Home', 'msg':msg})
    return render(request, 'fechar.html', {'title':'Fechar caixa', 'caixa_atual':caixa_atual})

def dados(request):
    hoje = datetime.date.today().strftime('%Y-%m-%d')
    caixas = caixa.objects.filter(data__contains=hoje)
    caixa_atual = caixa.objects.latest('id')
    dinheiro = 0
    cartao = 0 
    entrega = 0
    for d in caixa.objects.filter(data__contains=hoje, obs='Dinheiro'):
        d_id = d.item
        int(d_id)
        item = comanda.objects.filter(id=d_id).get()
        dinheiro = dinheiro + item.total
    for c in caixa.objects.filter(data__contains=hoje, obs='Cartao'):
        c_id = c.item
        int(c_id)
        item = comanda.objects.filter(id=c_id).get()
        cartao = cartao + item.total
    for e in caixa.objects.filter(data__contains=hoje):
        e_id = e.item
        try: 
            int(e_id)
            cmd = comanda.objects.filter(id=e_id).get()
            cmd1 = cmd.produtos.all()
            for p in cmd1:
                prod = p.produto_item.nome
                if prod == 'Entrega':
                    entrega = entrega +1
        except:
            cmd = None
    if request.method == 'POST':
        data_inicio = request.POST.get('data_inicio')
        data_fim = request.POST.get('data_fim')
        caixas = caixa.objects.filter(data__range=(data_inicio,data_fim)).all()
        dinheiro = 0
        cartao = 0 
        entrega = 0
        for d in caixa.objects.filter(data__range=(data_inicio,data_fim), obs='Dinheiro'):
            d_id = d.item
            int(d_id)
            item = comanda.objects.filter(id=d_id).get()
            dinheiro = dinheiro + item.total
        for c in caixa.objects.filter(data__range=(data_inicio,data_fim), obs='Cartao'):
            c_id = c.item
            int(c_id)
            item = comanda.objects.filter(id=c_id).get()
            cartao = cartao + item.total
        for e in caixa.objects.filter(data__range=(data_inicio,data_fim)):
            e_id = e.item
            int(e_id)
            cmd = comanda.objects.filter(id=e_id).get()
            cmd1 = cmd.produtos.all()
            for p in cmd1:
                prod = p.produto_item.nome
                if prod == 'Entrega':
                    entrega = entrega +1
        return render(request, 'dados.html', {'title':'Dados', 'caixas':caixas, 'hoje':data1, 'caixa_atual':caixa_atual, 'dinheiro':dinheiro, 'cartao':cartao, 'entrega':entrega})    
    return render(request, 'dados.html', {'title':'Dados', 'caixas':caixas, 'hoje':hoje, 'caixa_atual':caixa_atual, 'dinheiro':dinheiro, 'cartao':cartao, 'entrega':entrega})