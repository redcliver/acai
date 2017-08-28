from django.shortcuts import render
from pedidos.models import comanda, adicional, acai, itemacai, mix, itemmix, casadinho, itemcasadinho
from caixa.models import caixa
from decimal import *

# Create your views here.
def pedidos(request):
    comanda_id = request.GET.get('comanda_id')
    pedido1 = request.GET.get('pedido')
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

def tamanho(request):
    pedido1 = request.GET.get('pedido')
    comanda_id = request.GET.get('comanda_id')
    return render(request, 'tamanho.html', {'title':'Tamanho', 'pedido1':pedido1, 'comanda_id':comanda_id})

def adicionais(request):
    item_acai_id = request.GET.get('item_acai_id')
    item_casadinho_id = request.GET.get('item_casadinho_id')
    item_mix_id = request.GET.get('item_mix_id')
    adicionais = adicional.objects.all()
    comanda_id = request.GET.get('comanda_id')
    try:
        item_acai_id = itemacai.objects.filter(id=item_acai_id).get()
    except:
        item_acai_id = None
    try:
        item_casadinho_id = itemcasadinho.objects.filter(id=item_casadinho_id).get()
    except:
        item_casadinho_id = None
    try:
        item_mix_id = itemmix.objects.filter(id=item_mix_id).get()
    except:
        item_mix_id = None

    if item_acai_id != None :
        adicionais = adicional.objects.all()
        comanda_id = request.GET.get('comanda_id')
        return render(request, 'adicionais.html', {'title':'Adicionais', 'adicionais':adicionais, 'item_acai_id':item_acai_id, 'comanda_id':comanda_id})
    if item_casadinho_id != None:
        adicionais = adicional.objects.all()
        comanda_id = request.GET.get('comanda_id')
        return render(request, 'adicionais.html', {'title':'Adicionais', 'adicionais':adicionais, 'item_casadinho_id':item_casadinho_id, 'comanda_id':comanda_id})
    if item_mix_id != None :
        adicionais = adicional.objects.all()
        comanda_id = request.GET.get('comanda_id')
        return render(request, 'adicionais.html', {'title':'Adicionais', 'adicionais':adicionais, 'item_mix_id':item_mix_id, 'comanda_id':comanda_id})

    return render(request, 'adicionais.html', {'title':'Adicionais', 'adicionais':adicionais, 'comanda_id':comanda_id})

def finalizar(request):
    pedido2 = request.POST.get('pedido')
    tamanho1 = request.POST.get('tamanho')
    acai1 = request.POST.get('item_acai_id')
    casadinho1 = request.POST.get('item_casadinho_id')
    mix1 = request.POST.get('item_mix_id')
    adicionais1 = request.POST.getlist('adicional2')
    comanda_id = request.POST.get('comanda_id')
    if adicionais1 == []:
        adicionais1 = None
    
    try: ##Item Acai
        acai1 = itemacai.objects.filter(id=acai1).get()
    except:
        acai1 = None
    try: ##Item Casadinho
        casadinho1 = itemcasadinho.objects.filter(id=casadinho1).get()
    except:
        casadinho1 = None
    try: ##Item Mix
        mix1 = itemmix.objects.filter(id=mix1).get()
    except:
        mix1 = None
    
    
    try: ## Comanda_id
        comanda_id =comanda.objects.filter(id=comanda_id).get()
    except:
        comanda_id = None
    try: ## pedido acai
        pedido_acai = acai.objects.filter(img=pedido2, tamanho=tamanho1).get()
    except:
        pedido_acai = None
    try: ## pedido Casadinho
        pedido_casadinho = casadinho.objects.filter(img=pedido2, tamanho=tamanho1).get()
    except:
        pedido_casadinho = None
    try: ##pedido mix
        pedido_mix = mix.objects.filter(img=pedido2, tamanho=tamanho1).get()
    except:
        pedido_mix = None
    if pedido_acai != None and tamanho1 != None and comanda_id == None and adicionais1 == None: ##add novo acai em nova comanda
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
    if pedido_casadinho != None and tamanho1 != None and comanda_id == None and adicionais1 == None: ##add novo casadinho em nova comanda
        total_pedido = pedido_casadinho.preco
        novo_item_casadinho = itemcasadinho(casadinho_item=pedido_casadinho, total=total_pedido)
        novo_item_casadinho.save()
        nova_comanda = comanda(total=total_pedido)
        nova_comanda.save()
        nova_comanda.casadinhos.add(novo_item_casadinho)
        nova_comanda.save()
        casadinhos1 = nova_comanda.casadinhos.all()
        comanda_id = nova_comanda.id
        return render(request, 'finalizar.html',{'title':'Fechamento', 'casadinhos1':casadinhos1, 'comanda_id':comanda_id})
    if pedido_mix != None and tamanho1 != None and comanda_id == None and adicionais1 == None: ##add novo mix em nova comanda
        total_pedido = pedido_mix.preco
        novo_item_mix = itemmix(mix_item=pedido_mix, total=total_pedido)
        novo_item_mix.save()
        nova_comanda = comanda(total=total_pedido)
        nova_comanda.save()
        nova_comanda.mixs.add(novo_item_mix)
        nova_comanda.save()
        mixs1 = nova_comanda.mixs.all()
        comanda_id = nova_comanda.id
        return render(request, 'finalizar.html',{'title':'Fechamento', 'mixs1':mixs1, 'comanda_id':comanda_id})
    if acai1 != None and adicionais1 != None and comanda_id != None and pedido2 == None: ## add adicional em acai
        acai1 = acai1.id
        comanda_atual = comanda_id
        item_adicional = itemacai.objects.filter(id=acai1).get()
        for adicional2 in adicionais1 :
            add_id = int(adicional2)
            addicional = adicional.objects.filter(id=add_id).get()
            item_adicional.adicionais.add(addicional)
            item_adicional.total = item_adicional.total + addicional.preco
            item_adicional.save()
            comanda_atual.total = comanda_atual.total +addicional.preco
            comanda_atual.save()
        acais1 = comanda_atual.acais.all()
        mixs1 = comanda_atual.mixs.all()
        casadinhos1 = comanda_atual.casadinhos.all()
        return render(request, 'finalizar.html',{'title':'Fechamento', 'acais1':acais1, 'mixs1':mixs1, 'casadinhos1':casadinhos1, 'comanda_id':comanda_atual})
    if mix1 != None and adicionais1 != None and comanda_id != None and pedido2 == None: ## add adicional em mix
        mix1 = mix1.id
        comanda_atual = comanda_id
        item_adicional = itemmix.objects.filter(id=mix1).get()
        for adicional2 in adicionais1 :
            add_id = int(adicional2)
            addicional = adicional.objects.filter(id=add_id).get()
            item_adicional.adicionais.add(addicional)
            item_adicional.total = item_adicional.total + addicional.preco
            item_adicional.save()
            comanda_atual.total = comanda_atual.total +addicional.preco
            comanda_atual.save()
        acais1 = comanda_atual.acais.all()
        mixs1 = comanda_atual.mixs.all()
        casadinhos1 = comanda_atual.casadinhos.all()
        return render(request, 'finalizar.html',{'title':'Fechamento', 'acais1':acais1, 'mixs1':mixs1, 'casadinhos1':casadinhos1, 'comanda_id':comanda_atual})
    if casadinho1 != None and adicionais1 != None and comanda_id != None and pedido2 == None: ## add adicional em casadinho
        casadinho1 = casadinho1.id
        comanda_atual = comanda_id
        item_adicional = itemcasadinho.objects.filter(id=casadinho1).get()
        for adicional2 in adicionais1 :
            add_id = int(adicional2)
            addicional = adicional.objects.filter(id=add_id).get()
            item_adicional.adicionais.add(addicional)
            item_adicional.total = item_adicional.total + addicional.preco
            item_adicional.save()
            comanda_atual.total = comanda_atual.total +addicional.preco
            comanda_atual.save()
        acais1 = comanda_atual.acais.all()
        mixs1 = comanda_atual.mixs.all()
        casadinhos1 = comanda_atual.casadinhos.all()
        return render(request, 'finalizar.html',{'title':'Fechamento', 'acais1':acais1, 'mixs1':mixs1, 'casadinhos1':casadinhos1, 'comanda_id':comanda_atual})
    if pedido_acai != None and tamanho1 != None and comanda_id != None and adicionais1 == None: ##add novo acai em comanda existente
        comanda_atual = comanda_id
        pedido_acai = acai.objects.filter(img=pedido2, tamanho=tamanho1).get()
        total_pedido = pedido_acai.preco
        novo_item_acai = itemacai(acai_item=pedido_acai, total=total_pedido)
        novo_item_acai.save()
        comanda_atual.total = comanda_atual.total + total_pedido
        comanda_atual.save()
        comanda_atual.acais.add(novo_item_acai,)
        comanda_atual.save()
        acais1 = comanda_atual.acais.all()
        mixs1 = comanda_atual.mixs.all()
        casadinhos1 = comanda_atual.casadinhos.all()
        comanda_id = comanda_atual.id
        return render(request, 'finalizar.html', {'title':'Fechamento', 'acais1':acais1, 'mixs1':mixs1, 'casadinhos1':casadinhos1, 'comanda_id':comanda_id})
    if pedido_mix != None and tamanho1 != None and comanda_id != None and adicionais1 == None: ##add novo mix em comanda existente
        comanda_atual = comanda_id
        pedido_mix = mix.objects.filter(img=pedido2, tamanho=tamanho1).get()
        total_pedido = pedido_mix.preco
        novo_item_mix = itemmix(mix_item=pedido_mix, total=total_pedido)
        novo_item_mix.save()
        comanda_atual.total = comanda_atual.total + total_pedido
        comanda_atual.save()
        comanda_atual.mixs.add(novo_item_mix,)
        comanda_atual.save()
        mixs1 = comanda_atual.mixs.all()
        acais1 = comanda_atual.acais.all()
        casadinhos1 = comanda_atual.casadinhos.all()
        comanda_id = comanda_atual.id
        return render(request, 'finalizar.html', {'title':'Fechamento', 'acais1':acais1, 'mixs1':mixs1, 'casadinhos1':casadinhos1, 'comanda_id':comanda_id})
    if pedido_casadinho != None and tamanho1 != None and comanda_id != None and adicionais1 == None: ##add novo casadinho em comanda existente
        comanda_atual = comanda_id
        pedido_casadinho = casadinho.objects.filter(img=pedido2, tamanho=tamanho1).get()
        total_pedido = pedido_casadinho.preco
        novo_item_casadinho = itemcasadinho(casadinho_item=pedido_casadinho, total=total_pedido)
        novo_item_casadinho.save()
        comanda_atual.total = comanda_atual.total + total_pedido
        comanda_atual.save()
        comanda_atual.casadinhos.add(novo_item_casadinho,)
        comanda_atual.save()
        mixs1 = comanda_atual.mixs.all()
        acais1 = comanda_atual.acais.all()
        casadinhos1 = comanda_atual.casadinhos.all()
        comanda_id = comanda_atual.id
        return render(request, 'finalizar.html', {'title':'Fechamento', 'acais1':acais1, 'mixs1':mixs1, 'casadinhos1':casadinhos1, 'comanda_id':comanda_id})
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