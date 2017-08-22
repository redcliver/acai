from django.shortcuts import render
from pedidos.models import comanda, adicional, acai, itemacai
from caixa.models import caixa
from decimal import *

# Create your views here.
def pedidos(request):
    comanda_id = request.GET.get('comanda_id')
    if request.method == 'GET' and request.GET.get('pedido') != None:
        pedido1 = request.GET.get('pedido')
        comanda_id = request.GET.get('comanda_id')
        if pedido1 == 'acai':
            return render(request, 'acai.html', {'title':'Acai', 'comanda_id':comanda_id})
        if pedido1 == 'casadinho':
            return render(request, 'casadinho.html', {'title':'Casadinho', 'comanda_id':comanda_id})
        if pedido1 == 'mix':
            return render(request, 'mix.html', {'title':'Mix', 'comanda_id':comanda_id})
        if pedido1 == 'acaienergy':
            return render(request, 'acaienergy.html', {'title':'acaienergy', 'comanda_id':comanda_id})
        if pedido1 == 'acaicreme':
            return render(request, 'acaicreme.html', {'title':'acaicreme', 'comanda_id':comanda_id})
        if pedido1 == 'sorvete':
            return render(request, 'sorvete.html', {'title':'sorvete', 'comanda_id':comanda_id})
        if pedido1 == 'milkshake':
            return render(request, 'milkshake.html', {'title':'milkshake', 'comanda_id':comanda_id})
        if pedido1 == 'petit':
            return render(request, 'petit.html', {'title':'petit', 'comanda_id':comanda_id})
        if pedido1 == 'fondue':
            return render(request, 'fondue.html', {'title':'fondue', 'comanda_id':comanda_id})
        if pedido1 == 'sucos':
            return render(request, 'sucos.html', {'title':'sucos', 'comanda_id':comanda_id})
        if pedido1 == 'produtos':
            return render(request, 'produtos.html', {'title':'produtos', 'comanda_id':comanda_id})
        return render(request, 'pedidos.html', {'title':'Pedidos', 'comanda_id':comanda_id})
    return render(request, 'pedidos.html', {'title':'Pedidos', 'comanda_id':comanda_id})

def tamanho(request):
    pedido1 = request.GET.get('pedido')
    comanda_id = request.GET.get('comanda_id')
    return render(request, 'tamanho.html', {'title':'Tamanho', 'pedido1':pedido1, 'comanda_id':comanda_id})

def adicionais(request):
    item_id = request.GET.get('item_id')
    item_atual = itemacai.objects.filter(id=item_id).get()
    adicionais = adicional.objects.all()
    comanda_id = request.GET.get('comanda_id')
    return render(request, 'adicionais.html', {'title':'Adicionais', 'adicionais':adicionais, 'item_atual':item_atual, 'comanda_id':comanda_id})

def finalizar(request):
    pedido2 = request.POST.get('pedido')
    tamanho1 = request.POST.get('tamanho')
    item_id = request.POST.get('item_id')
    comanda_id = request.POST.get('comanda_id')
    adicionais1 = request.POST.getlist('adicional2')
    if pedido2 != None and tamanho1 != None and comanda_id == 'None':
        pedido2 = request.POST.get('pedido')
        tamanho1 = request.POST.get('tamanho')
        item_id = request.POST.get('item_id')
        pedido_acai = acai.objects.filter(img=pedido2, tamanho=tamanho1).get()
        total_pedido = pedido_acai.preco
        novo_item_acai = itemacai(acai_item=pedido_acai, total=total_pedido)
        novo_item_acai.save()
        nova_comanda = comanda(total=total_pedido)
        nova_comanda.save()
        nova_comanda.acais.add(novo_item_acai)
        nova_comanda.save()
        acais1 = nova_comanda.acais.all()
        comanda_id = nova_comanda.id
        return render(request, 'finalizar.html',{'title':'Fechamento', 'acais1':acais1, 'comanda_id':comanda_id})
    if request.method == 'POST' and item_id != None:
        comanda_id = request.POST.get('comanda_id')
        item_id = request.POST.get('item_id')
        comanda_atual = comanda.objects.filter(id=comanda_id).get()
        item_adicional = itemacai.objects.filter(id=item_id).get()
        for adicional2 in adicionais1 :
            add_id = int(adicional2)
            addicional = adicional.objects.get(id=add_id)
            item_adicional.adicionais.add(addicional)
            item_adicional.total = item_adicional.total + addicional.preco
            item_adicional.save()
            comanda_atual.total = comanda_atual.total +addicional.preco
            comanda_atual.save()
        acais1 = comanda_atual.acais.all()
        return render(request, 'finalizar.html',{'title':'Fechamento', 'acais1':acais1, 'comanda_id':comanda_id})
    if pedido2 != None and tamanho1 != None and comanda_id != None:
        pedido2 = request.POST.get('pedido')
        tamanho1 = request.POST.get('tamanho')
        comanda_id = request.POST.get('comanda_id')
        comanda_atual = comanda.objects.filter(id=comanda_id).get()
        pedido_acai = acai.objects.filter(img=pedido2, tamanho=tamanho1).get()
        total_pedido = pedido_acai.preco
        novo_item_acai = itemacai(acai_item=pedido_acai, total=total_pedido)
        novo_item_acai.save()
        comanda_atual.total = comanda_atual.total + total_pedido
        comanda_atual.save()
        comanda_atual.acais.add(novo_item_acai,)
        comanda_atual.save()
        acais1 = comanda_atual.acais.all()
        comanda_id = comanda_atual.id
        return render(request, 'finalizar.html', {'title':'Fechamento', 'acais1':acais1, 'comanda_id':comanda_id})
    return render(request, 'finalizar.html',{'title':'Fechamento','comanda_id':comanda_id})

def metodo(request):
    comanda_id = request.GET.get('comanda_id')
    comanda_atual = comanda.objects.filter(id=comanda_id).get()

    return render(request, 'metodo.html', {'title':'Metodo de pagamento', 'comanda_atual':comanda_atual})

def dinheiro(request):
    comanda_id = request.GET.get('comanda_id')
    comanda_atual = comanda.objects.filter(id=comanda_id).get()
    caixa_atual = caixa.objects.latest('id')
    item_caixa = "Comanda numero : "+str(comanda_atual.id)
    metodo_caixa = "Dinheiro"
    novo_total = caixa_atual.total + comanda_atual.total
    nova_entrada = caixa(total=novo_total, item=item_caixa, obs=metodo_caixa)
    nova_entrada.save()
    return render(request, 'dinheiro.html',{'title':'Pagamento em dinheiro', 'comanda_atual':comanda_atual})

def cartao(request):
    comanda_id = request.GET.get('comanda_id')
    comanda_atual = comanda.objects.filter(id=comanda_id).get()
    caixa_atual = caixa.objects.latest('id')
    item_caixa = "Comanda numero : "+str(comanda_atual.id)
    metodo_caixa = "Cartao"
    novo_total = caixa_atual.total + comanda_atual.total
    nova_entrada = caixa(total=novo_total, item=item_caixa, obs=metodo_caixa)
    nova_entrada.save()
    return render(request, 'cartao.html',{'title':'Pagamento em cartao', 'comanda_atual':comanda_atual})

def troco(request):
    comanda_id = request.GET.get('comanda_id')
    comanda_atual = comanda.objects.filter(id=comanda_id).get()
    recebido = request.GET.get('recebido')
    troco = Decimal(recebido) - comanda_atual.total  
    return render(request, 'troco.html',{'title':'Troco', 'comanda_atual':comanda_atual, 'troco':troco, 'recebido':recebido})