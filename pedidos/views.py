from django.shortcuts import render
from pedidos.models import comanda, produto, sorvete ,itemsorvete , itemproduto, adicional, acai, itemacai, mix, itemmix, casadinho, itemcasadinho, creme, itemcreme, mshake, itemmshake, petit, itempetit, fondue, itemfondue, suco, itemsuco
from caixa.models import caixa
from decimal import *
from escposprinter import *

# Create your views here.
def pedidos(request):
    comanda_id = request.GET.get('comanda_id')
    pedido1 = request.GET.get('pedido')
    if pedido1 == 'acai':
        return render(request, 'acai.html', {'title':'Acai na Tigela', 'comanda_id':comanda_id})
    if pedido1 == 'casadinho':
        return render(request, 'casadinho.html', {'title':'Açaí Casadinho', 'comanda_id':comanda_id})
    if pedido1 == 'mix':
        return render(request, 'mix.html', {'title':'Açaí Mix', 'comanda_id':comanda_id})
    if pedido1 == 'acaienergy':
        return render(request, 'acaienergy.html', {'title':'Açaí Energy', 'comanda_id':comanda_id})
    if pedido1 == 'acaicreme':
        return render(request, 'acaicreme.html', {'title':'Cremes', 'comanda_id':comanda_id})
    if pedido1 == 'sorvete':
        return render(request, 'sorvete.html', {'title':'sorvete', 'comanda_id':comanda_id})
    if pedido1 == 'milkshake':
        return render(request, 'milkshake.html', {'title':'Milk Shake', 'comanda_id':comanda_id})
    if pedido1 == 'petit':
        return render(request, 'petit.html', {'title':'Petit Gateau', 'comanda_id':comanda_id})
    if pedido1 == 'fondue':
        return render(request, 'fondue.html', {'title':'Fondue', 'comanda_id':comanda_id})
    if pedido1 == 'sucos':
        return render(request, 'sucos.html', {'title':'Sucos', 'comanda_id':comanda_id})
    if pedido1 == 'produtos':
        return render(request, 'produtos.html', {'title':'Produtos', 'comanda_id':comanda_id})

    return render(request, 'pedidos.html', {'title':'Pedidos', 'comanda_id':comanda_id})

def tamanho(request):
    pedido1 = request.GET.get('pedido')
    comanda_id = request.GET.get('comanda_id')
    return render(request, 'tamanho.html', {'title':'Tamanho', 'pedido1':pedido1, 'comanda_id':comanda_id})

def confirmacao(request):
    pedido1 = request.GET.get('pedido')
    comanda_id = request.GET.get('comanda_id')
    return render(request, 'confirmacao.html', {'title':'Confirmação', 'pedido1':pedido1, 'comanda_id':comanda_id})

def adicionais(request):
    item_acai_id = request.GET.get('item_acai_id')
    item_casadinho_id = request.GET.get('item_casadinho_id')
    item_mix_id = request.GET.get('item_mix_id')
    item_creme_id = request.GET.get('item_creme_id')
    item_sorvete_id = request.GET.get('item_sorvete_id')
    item_mshake_id = request.GET.get('item_mshake_id')
    item_petit_id = request.GET.get('item_petit_id')
    item_fondue_id = request.GET.get('item_fondue_id')
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
    try:
        item_creme_id = itemcreme.objects.filter(id=item_creme_id).get()
    except:
        item_creme_id = None
    try:
        item_sorvete_id = itemsorvete.objects.filter(id=item_sorvete_id).get()
    except:
        item_sorvete_id = None
    try:
        item_mshake_id = itemmshake.objects.filter(id=item_mshake_id).get()
    except:
        item_mshake_id = None
    try:
        item_petit_id = itempetit.objects.filter(id=item_petit_id).get()
    except:
        item_petit_id = None
    try:
        item_fondue_id = itemfondue.objects.filter(id=item_fondue_id).get()
    except:
        item_fondue_id = None

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
    if item_creme_id != None :
        adicionais = adicional.objects.all()
        comanda_id = request.GET.get('comanda_id')
        return render(request, 'adicionais.html', {'title':'Adicionais', 'adicionais':adicionais, 'item_creme_id':item_creme_id, 'comanda_id':comanda_id})
    if item_sorvete_id != None :
        adicionais = adicional.objects.all()
        comanda_id = request.GET.get('comanda_id')
        return render(request, 'adicionais.html', {'title':'Adicionais', 'adicionais':adicionais, 'item_sorvete_id':item_sorvete_id, 'comanda_id':comanda_id})
    if item_mshake_id != None :
        adicionais = adicional.objects.all()
        comanda_id = request.GET.get('comanda_id')
        return render(request, 'adicionais.html', {'title':'Adicionais', 'adicionais':adicionais, 'item_mshake_id':item_mshake_id, 'comanda_id':comanda_id})
    if item_petit_id != None :
        adicionais = adicional.objects.all()
        comanda_id = request.GET.get('comanda_id')
        return render(request, 'adicionais.html', {'title':'Adicionais', 'adicionais':adicionais, 'item_petit_id':item_petit_id, 'comanda_id':comanda_id})
    if item_fondue_id != None :
        adicionais = adicional.objects.all()
        comanda_id = request.GET.get('comanda_id')
        return render(request, 'adicionais.html', {'title':'Adicionais', 'adicionais':adicionais, 'item_fondue_id':item_fondue_id, 'comanda_id':comanda_id})
    return render(request, 'adicionais.html', {'title':'Adicionais', 'adicionais':adicionais, 'comanda_id':comanda_id})

def finalizar(request):
    pedido2 = request.POST.get('pedido')
    tamanho1 = request.POST.get('tamanho')
    acai1 = request.POST.get('item_acai_id')
    casadinho1 = request.POST.get('item_casadinho_id')
    mix1 = request.POST.get('item_mix_id')
    creme1 = request.POST.get('item_creme_id')
    sorvete1 = request.POST.get('item_sorvete_id')
    mshake1 = request.POST.get('item_mshake_id')
    petit1 = request.POST.get('item_petit_id')
    fondue1 = request.POST.get('item_fondue_id')
    pedido_produto = request.POST.get('pedido_produto')
    pedido_sorvete = request.POST.get('pedido_produto')
    pedido_petit = request.POST.get('pedido_produto')
    pedido_fondue = request.POST.get('pedido_produto')
    pedido_suco = request.POST.get('pedido_produto')
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
    try: ##Item Creme
        creme1 = itemcreme.objects.filter(id=creme1).get()
    except:
        creme1 = None
    try: ##Item Produto
        produto1 = itemproduto.objects.filter(id=produto1).get()
    except:
        produto1 = None
    try: ##Item Sorvete
        sorvete1 = itemsorvete.objects.filter(id=sorvete1).get()
    except:
        sorvete1 = None
    try: ##Item MShake
        mshake1 = itemmshake.objects.filter(id=mshake1).get()
    except:
        mshake1 = None
    try: ##Item Petit
        petit1 = itempetit.objects.filter(id=petit1).get()
    except:
        petit1 = None
    try: ##Item Fondue
        fondue1 = itemfondue.objects.filter(id=fondue1).get()
    except:
        fondue1 = None
    
    try: ## Comanda_id
        comanda_id = comanda.objects.filter(id=comanda_id).get()
    except:
        comanda_id = None
    try: ## pedido produto
        pedido_produto = produto.objects.filter(img=pedido_produto).get()
    except:
        pedido_produto = None
    try: ## pedido petit
        pedido_petit = petit.objects.filter(img=pedido_petit).get()
    except:
        pedido_petit = None
    try: ## pedido fondue
        pedido_fondue = fondue.objects.filter(img=pedido_fondue).get()
    except:
        pedido_fondue = None
    try: ## pedido suco
        pedido_suco = suco.objects.filter(img=pedido_suco).get()
    except:
        pedido_suco = None
    try: ## pedido sorvete
        pedido_sorvete = sorvete.objects.filter(img=pedido_sorvete).get()
    except:
        pedido_sorvete = None
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
    try: ##pedido creme
        pedido_creme = creme.objects.filter(img=pedido2, tamanho=tamanho1).get()
    except:
        pedido_creme = None
    try: ##pedido mshake
        pedido_mshake = mshake.objects.filter(img=pedido2, tamanho=tamanho1).get()
    except:
        pedido_mshake = None

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
    if pedido_creme != None and tamanho1 != None and comanda_id == None and adicionais1 == None: ##add novo creme em nova comanda
        total_pedido = pedido_creme.preco
        novo_item_creme = itemcreme(creme_item=pedido_creme, total=total_pedido)
        novo_item_creme.save()
        nova_comanda = comanda(total=total_pedido)
        nova_comanda.save()
        nova_comanda.cremes.add(novo_item_creme)
        nova_comanda.save()
        cremes1 = nova_comanda.cremes.all()
        comanda_id = nova_comanda.id
        return render(request, 'finalizar.html',{'title':'Fechamento', 'cremes1':cremes1, 'comanda_id':comanda_id})
    if pedido_produto != None and comanda_id == None and adicionais1 == None: ##add novo produto em nova comanda
        total_pedido = pedido_produto.preco
        novo_item_produto = itemproduto(produto_item=pedido_produto, total=total_pedido)
        novo_item_produto.save()
        nova_comanda = comanda(total=total_pedido)
        nova_comanda.save()
        nova_comanda.produtos.add(novo_item_produto)
        nova_comanda.save()
        produtos1 = nova_comanda.produtos.all()
        comanda_id = nova_comanda.id
        return render(request, 'finalizar.html',{'title':'Fechamento', 'produtos1':produtos1, 'comanda_id':comanda_id})
    if pedido_sorvete != None and comanda_id == None and adicionais1 == None: ##add novo sorvete em nova comanda
        total_pedido = pedido_sorvete.preco
        novo_item_sorvete = itemsorvete(sorvete_item=pedido_sorvete, total=total_pedido)
        novo_item_sorvete.save()
        nova_comanda = comanda(total=total_pedido)
        nova_comanda.save()
        nova_comanda.sorvetes.add(novo_item_sorvete)
        nova_comanda.save()
        sorvetes1 = nova_comanda.sorvetes.all()
        comanda_id = nova_comanda.id
        return render(request, 'finalizar.html',{'title':'Fechamento', 'sorvetes1':sorvetes1, 'comanda_id':comanda_id})
    if pedido_mshake != None and comanda_id == None and adicionais1 == None: ##add novo mshake em nova comanda
        total_pedido = pedido_mshake.preco
        novo_item_mshake = itemmshake(mshake_item=pedido_mshake, total=total_pedido)
        novo_item_mshake.save()
        nova_comanda = comanda(total=total_pedido)
        nova_comanda.save()
        nova_comanda.mshakes.add(novo_item_mshake)
        nova_comanda.save()
        mshakes1 = nova_comanda.mshakes.all()
        comanda_id = nova_comanda.id
        return render(request, 'finalizar.html',{'title':'Fechamento', 'mshakes1':mshakes1, 'comanda_id':comanda_id})
    if pedido_petit != None and comanda_id == None and adicionais1 == None: ##add novo petit em nova comanda
        total_pedido = pedido_petit.preco
        novo_item_petit = itempetit(petit_item=pedido_petit, total=total_pedido)
        novo_item_petit.save()
        nova_comanda = comanda(total=total_pedido)
        nova_comanda.save()
        nova_comanda.petits.add(novo_item_petit)
        nova_comanda.save()
        petits1 = nova_comanda.petits.all()
        comanda_id = nova_comanda.id
        return render(request, 'finalizar.html',{'title':'Fechamento', 'petits1':petits1, 'comanda_id':comanda_id})
    if pedido_fondue != None and comanda_id == None and adicionais1 == None: ##add novo fondue em nova comanda
        total_pedido = pedido_fondue.preco
        novo_item_fondue = itemfondue(fondue_item=pedido_fondue, total=total_pedido)
        novo_item_fondue.save()
        nova_comanda = comanda(total=total_pedido)
        nova_comanda.save()
        nova_comanda.fondues.add(novo_item_fondue)
        nova_comanda.save()
        fondues1 = nova_comanda.fondues.all()
        comanda_id = nova_comanda.id
        return render(request, 'finalizar.html',{'title':'Fechamento', 'fondues1':fondues1, 'comanda_id':comanda_id})
    if pedido_suco != None and comanda_id == None and adicionais1 == None: ##add novo suco em nova comanda
        total_pedido = pedido_suco.preco
        novo_item_suco = itemsuco(suco_item=pedido_suco, total=total_pedido)
        novo_item_suco.save()
        nova_comanda = comanda(total=total_pedido)
        nova_comanda.save()
        nova_comanda.sucos.add(novo_item_suco)
        nova_comanda.save()
        sucos1 = nova_comanda.sucos.all()
        comanda_id = nova_comanda.id
        return render(request, 'finalizar.html',{'title':'Fechamento', 'sucos1':sucos1, 'comanda_id':comanda_id})
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
        produtos1 = comanda_atual.produtos.all()
        cremes1 = comanda_atual.cremes.all()
        sorvetes1 = comanda_atual.sorvetes.all()
        mshakes1 = comanda_atual.mshakes.all()
        petits1 = comanda_atual.petits.all()
        fondues1 = comanda_atual.fondues.all()
        return render(request, 'finalizar.html',{'title':'Fechamento', 'fondues1':fondues1, 'petits1':petits1, 'mshakes1':mshakes1, 'sorvetes1':sorvetes1, 'acais1':acais1, 'mixs1':mixs1, 'casadinhos1':casadinhos1, 'cremes1':cremes1, 'produtos1':produtos1, 'comanda_id':comanda_atual})
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
        produtos1 = comanda_atual.produtos.all()
        cremes1 = comanda_atual.cremes.all()
        sorvetes1 = comanda_atual.sorvetes.all()
        mshakes1 = comanda_atual.mshakes.all()
        petits1 = comanda_atual.petits.all()
        fondues1 = comanda_atual.fondues.all()
        return render(request, 'finalizar.html',{'title':'Fechamento', 'fondues1':fondues1, 'petits1':petits1, 'mshakes1':mshakes1, 'sorvetes1':sorvetes1, 'acais1':acais1, 'mixs1':mixs1, 'casadinhos1':casadinhos1, 'cremes1':cremes1, 'produtos1':produtos1, 'comanda_id':comanda_atual})
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
        produtos1 = comanda_atual.produtos.all()
        cremes1 = comanda_atual.cremes.all()
        sorvetes1 = comanda_atual.sorvetes.all()
        mshakes1 = comanda_atual.mshakes.all()
        petits1 = comanda_atual.petits.all()
        fondues1 = comanda_atual.fondues.all()
        return render(request, 'finalizar.html',{'title':'Fechamento', 'fondues1':fondues1, 'petits1':petits1, 'mshakes1':mshakes1, 'sorvetes1':sorvetes1, 'acais1':acais1, 'mixs1':mixs1, 'casadinhos1':casadinhos1, 'cremes1':cremes1, 'produtos1':produtos1, 'comanda_id':comanda_atual})
    if creme1 != None and adicionais1 != None and comanda_id != None and pedido2 == None: ## add adicional em creme
        creme1 = creme1.id
        comanda_atual = comanda_id
        item_adicional = itemcreme.objects.filter(id=creme1).get()
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
        produtos1 = comanda_atual.produtos.all()
        cremes1 = comanda_atual.cremes.all()
        sorvetes1 = comanda_atual.sorvetes.all()
        mshakes1 = comanda_atual.mshakes.all()
        petits1 = comanda_atual.petits.all()
        fondues1 = comanda_atual.fondues.all()
        return render(request, 'finalizar.html',{'title':'Fechamento', 'fondues1':fondues1, 'petits1':petits1, 'mshakes1':mshakes1, 'sorvetes1':sorvetes1, 'acais1':acais1, 'mixs1':mixs1, 'casadinhos1':casadinhos1, 'cremes1':cremes1, 'produtos1':produtos1, 'comanda_id':comanda_atual})
    if sorvete1 != None and adicionais1 != None and comanda_id != None and pedido2 == None: ## add adicional em sorvete
        sorvete1 = sorvete1.id
        comanda_atual = comanda_id
        item_adicional = itemsorvete.objects.filter(id=sorvete1).get()
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
        produtos1 = comanda_atual.produtos.all()
        cremes1 = comanda_atual.cremes.all()
        sorvetes1 = comanda_atual.sorvetes.all()
        mshakes1 = comanda_atual.mshakes.all()
        petits1 = comanda_atual.petits.all()
        fondues1 = comanda_atual.fondues.all()
        return render(request, 'finalizar.html',{'title':'Fechamento', 'fondues1':fondues1, 'petits1':petits1, 'mshakes1':mshakes1, 'sorvetes1':sorvetes1, 'acais1':acais1, 'mixs1':mixs1, 'casadinhos1':casadinhos1, 'cremes1':cremes1, 'produtos1':produtos1, 'comanda_id':comanda_atual})
    if mshake1 != None and adicionais1 != None and comanda_id != None and pedido2 == None: ## add adicional em mshake
        mshake1 = mshake1.id
        comanda_atual = comanda_id
        item_adicional = itemmshake.objects.filter(id=mshake1).get()
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
        cremes1 = comanda_atual.cremes.all()
        produtos1 = comanda_atual.produtos.all()
        sorvetes1 = comanda_atual.sorvetes.all()
        mshakes1 = comanda_atual.mshakes.all()
        petits1 = comanda_atual.petits.all()
        fondues1 = comanda_atual.fondues.all()
        return render(request, 'finalizar.html',{'title':'Fechamento', 'fondues1':fondues1, 'petits1':petits1, 'mshakes1':mshakes1, 'sorvetes1':sorvetes1, 'acais1':acais1, 'mixs1':mixs1, 'casadinhos1':casadinhos1, 'cremes1':cremes1, 'produtos1':produtos1, 'comanda_id':comanda_atual})
    if petit1 != None and adicionais1 != None and comanda_id != None and pedido2 == None: ## add adicional em petit
        petit1 = petit1.id
        comanda_atual = comanda_id
        item_adicional = itempetit.objects.filter(id=petit1).get()
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
        cremes1 = comanda_atual.cremes.all()
        produtos1 = comanda_atual.produtos.all()
        sorvetes1 = comanda_atual.sorvetes.all()
        mshakes1 = comanda_atual.mshakes.all()
        petits1 = comanda_atual.petits.all()
        fondues1 = comanda_atual.fondues.all()
        return render(request, 'finalizar.html',{'title':'Fechamento', 'fondues1':fondues1, 'petits1':petits1, 'mshakes1':mshakes1, 'sorvetes1':sorvetes1, 'acais1':acais1, 'mixs1':mixs1, 'casadinhos1':casadinhos1, 'cremes1':cremes1, 'produtos1':produtos1, 'comanda_id':comanda_atual})
    if fondue1 != None and adicionais1 != None and comanda_id != None and pedido2 == None: ## add adicional em fondue
        fondue1 = fondue1.id
        comanda_atual = comanda_id
        item_adicional = itemfondue.objects.filter(id=fondue1).get()
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
        cremes1 = comanda_atual.cremes.all()
        produtos1 = comanda_atual.produtos.all()
        sorvetes1 = comanda_atual.sorvetes.all()
        mshakes1 = comanda_atual.mshakes.all()
        petits1 = comanda_atual.petits.all()
        fondues1 = comanda_atual.fondues.all()
        return render(request, 'finalizar.html',{'title':'Fechamento', 'fondues1':fondues1, 'petits1':petits1, 'mshakes1':mshakes1, 'sorvetes1':sorvetes1, 'acais1':acais1, 'mixs1':mixs1, 'casadinhos1':casadinhos1, 'cremes1':cremes1, 'produtos1':produtos1, 'comanda_id':comanda_atual})
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
        cremes1 = comanda_atual.cremes.all()
        produtos1 = comanda_atual.produtos.all()
        sorvetes1 = comanda_atual.sorvetes.all()
        mshakes1 = comanda_atual.mshakes.all()
        petits1 = comanda_atual.petits.all()
        fondues1 = comanda_atual.fondues.all()
        sucos1 = comanda_atual.sucos.all()
        comanda_id = comanda_atual.id
        return render(request, 'finalizar.html', {'title':'Fechamento', 'sucos1':sucos1, 'fondues1':fondues1, 'petits1':petits1, 'mshakes1':mshakes1, 'sorvetes1':sorvetes1, 'acais1':acais1, 'mixs1':mixs1, 'casadinhos1':casadinhos1, 'cremes1':cremes1, 'produtos1':produtos1, 'comanda_id':comanda_id})
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
        cremes1 = comanda_atual.cremes.all()
        produtos1 = comanda_atual.produtos.all()
        sorvetes1 = comanda_atual.sorvetes.all()
        mshakes1 = comanda_atual.mshakes.all()
        petits1 = comanda_atual.petits.all()
        fondues1 = comanda_atual.fondues.all()
        sucos1 = comanda_atual.sucos.all()
        comanda_id = comanda_atual.id
        return render(request, 'finalizar.html', {'title':'Fechamento', 'sucos1':sucos1, 'fondues1':fondues1, 'petits1':petits1, 'mshakes1':mshakes1, 'sorvetes1':sorvetes1, 'acais1':acais1, 'mixs1':mixs1, 'casadinhos1':casadinhos1, 'cremes1':cremes1, 'produtos1':produtos1, 'comanda_id':comanda_id})
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
        cremes1 = comanda_atual.cremes.all()
        produtos1 = comanda_atual.produtos.all()
        sorvetes1 = comanda_atual.sorvetes.all()
        mshakes1 = comanda_atual.mshakes.all()
        petits1 = comanda_atual.petits.all()
        fondues1 = comanda_atual.fondues.all()
        sucos1 = comanda_atual.sucos.all()
        comanda_id = comanda_atual.id
        return render(request, 'finalizar.html', {'title':'Fechamento', 'sucos1':sucos1, 'fondues1':fondues1, 'petits1':petits1, 'mshakes1':mshakes1, 'sorvetes1':sorvetes1, 'acais1':acais1, 'mixs1':mixs1, 'casadinhos1':casadinhos1, 'cremes1':cremes1, 'produtos1':produtos1, 'comanda_id':comanda_id})
    if pedido_creme != None and tamanho1 != None and comanda_id != None and adicionais1 == None: ##add novo creme em comanda existente
        comanda_atual = comanda_id
        pedido_creme = creme.objects.filter(img=pedido2, tamanho=tamanho1).get()
        total_pedido = pedido_creme.preco
        novo_item_creme = itemcreme(creme_item=pedido_creme, total=total_pedido)
        novo_item_creme.save()
        comanda_atual.total = comanda_atual.total + total_pedido
        comanda_atual.save()
        comanda_atual.cremes.add(novo_item_creme,)
        comanda_atual.save()
        mixs1 = comanda_atual.mixs.all()
        acais1 = comanda_atual.acais.all()
        casadinhos1 = comanda_atual.casadinhos.all()
        cremes1 = comanda_atual.cremes.all()
        produtos1 = comanda_atual.produtos.all()
        sorvetes1 = comanda_atual.sorvetes.all()
        mshakes1 = comanda_atual.mshakes.all()
        petits1 = comanda_atual.petits.all()
        fondues1 = comanda_atual.fondues.all()
        sucos1 = comanda_atual.sucos.all()
        comanda_id = comanda_atual.id
        return render(request, 'finalizar.html', {'title':'Fechamento', 'sucos1':sucos1, 'fondues1':fondues1, 'petits1':petits1, 'mshakes1':mshakes1, 'sorvetes1':sorvetes1, 'acais1':acais1, 'mixs1':mixs1, 'casadinhos1':casadinhos1, 'cremes1':cremes1, 'produtos1':produtos1, 'comanda_id':comanda_id})
    if pedido_sorvete != None and comanda_id != None and adicionais1 == None: ##add novo sorvete em comanda existente
        comanda_atual = comanda_id
        total_pedido = pedido_sorvete.preco
        novo_item_sorv = itemsorvete(sorvete_item=pedido_sorvete, total=total_pedido)
        novo_item_sorv.save()
        comanda_atual.total = comanda_atual.total + total_pedido
        comanda_atual.save()
        comanda_atual.sorvetes.add(novo_item_sorv,)
        comanda_atual.save()
        mixs1 = comanda_atual.mixs.all()
        acais1 = comanda_atual.acais.all()
        casadinhos1 = comanda_atual.casadinhos.all()
        cremes1 = comanda_atual.cremes.all()
        produtos1 = comanda_atual.produtos.all()
        sorvetes1 = comanda_atual.sorvetes.all()
        mshakes1 = comanda_atual.mshakes.all()
        petits1 = comanda_atual.petits.all()
        fondues1 = comanda_atual.fondues.all()
        sucos1 = comanda_atual.sucos.all()
        comanda_id = comanda_atual.id
        return render(request, 'finalizar.html', {'title':'Fechamento', 'sucos1':sucos1, 'fondues1':fondues1, 'petits1':petits1, 'mshakes1':mshakes1, 'sorvetes1':sorvetes1, 'acais1':acais1, 'mixs1':mixs1, 'casadinhos1':casadinhos1, 'cremes1':cremes1, 'produtos1':produtos1, 'comanda_id':comanda_id})
    if pedido_mshake != None and comanda_id != None and adicionais1 == None: ##add novo mshake em comanda existente
        comanda_atual = comanda_id
        total_pedido = pedido_mshake.preco
        novo_item_sorv = itemmshake(mshake_item=pedido_mshake, total=total_pedido)
        novo_item_sorv.save()
        comanda_atual.total = comanda_atual.total + total_pedido
        comanda_atual.save()
        comanda_atual.mshakes.add(novo_item_sorv,)
        comanda_atual.save()
        mixs1 = comanda_atual.mixs.all()
        acais1 = comanda_atual.acais.all()
        casadinhos1 = comanda_atual.casadinhos.all()
        cremes1 = comanda_atual.cremes.all()
        produtos1 = comanda_atual.produtos.all()
        sorvetes1 = comanda_atual.sorvetes.all()
        mshakes1 = comanda_atual.mshakes.all()
        petits1 = comanda_atual.petits.all()
        fondues1 = comanda_atual.fondues.all()
        sucos1 = comanda_atual.sucos.all()
        comanda_id = comanda_atual.id
        return render(request, 'finalizar.html', {'title':'Fechamento', 'sucos1':sucos1, 'fondues1':fondues1, 'petits1':petits1, 'mshakes1':mshakes1, 'sorvetes1':sorvetes1, 'acais1':acais1, 'mixs1':mixs1, 'casadinhos1':casadinhos1, 'cremes1':cremes1, 'produtos1':produtos1, 'comanda_id':comanda_id})
    if pedido_petit != None and comanda_id != None and adicionais1 == None: ##add novo ppetit em comanda existente
        comanda_atual = comanda_id
        total_pedido = pedido_petit.preco
        novo_item_petit = itempetit(petit_item=pedido_petit, total=total_pedido)
        novo_item_petit.save()
        comanda_atual.total = comanda_atual.total + total_pedido
        comanda_atual.save()
        comanda_atual.petits.add(novo_item_petit,)
        comanda_atual.save()
        mixs1 = comanda_atual.mixs.all()
        acais1 = comanda_atual.acais.all()
        casadinhos1 = comanda_atual.casadinhos.all()
        cremes1 = comanda_atual.cremes.all()
        produtos1 = comanda_atual.produtos.all()
        sorvetes1 = comanda_atual.sorvetes.all()
        mshakes1 = comanda_atual.mshakes.all()
        petits1 = comanda_atual.petits.all()
        fondues1 = comanda_atual.fondues.all()
        sucos1 = comanda_atual.sucos.all()
        comanda_id = comanda_atual.id
        return render(request, 'finalizar.html', {'title':'Fechamento', 'sucos1':sucos1, 'fondues1':fondues1, 'petits1':petits1, 'mshakes1':mshakes1, 'sorvetes1':sorvetes1, 'acais1':acais1, 'mixs1':mixs1, 'casadinhos1':casadinhos1, 'cremes1':cremes1, 'produtos1':produtos1, 'comanda_id':comanda_id})
    if pedido_fondue != None and comanda_id != None and adicionais1 == None: ##add novo fondue em comanda existente
        comanda_atual = comanda_id
        total_pedido = pedido_fondue.preco
        novo_item_fondue = itemfondue(fondue_item=pedido_fondue, total=total_pedido)
        novo_item_fondue.save()
        comanda_atual.total = comanda_atual.total + total_pedido
        comanda_atual.save()
        comanda_atual.fondues.add(novo_item_fondue,)
        comanda_atual.save()
        mixs1 = comanda_atual.mixs.all()
        acais1 = comanda_atual.acais.all()
        casadinhos1 = comanda_atual.casadinhos.all()
        cremes1 = comanda_atual.cremes.all()
        produtos1 = comanda_atual.produtos.all()
        sorvetes1 = comanda_atual.sorvetes.all()
        mshakes1 = comanda_atual.mshakes.all()
        petits1 = comanda_atual.petits.all()
        fondues1 = comanda_atual.fondues.all()
        sucos1 = comanda_atual.sucos.all()
        comanda_id = comanda_atual.id
        return render(request, 'finalizar.html', {'title':'Fechamento', 'sucos1':sucos1, 'fondues1':fondues1, 'petits1':petits1, 'mshakes1':mshakes1, 'sorvetes1':sorvetes1, 'acais1':acais1, 'mixs1':mixs1, 'casadinhos1':casadinhos1, 'cremes1':cremes1, 'produtos1':produtos1, 'comanda_id':comanda_id})
    if pedido_suco != None and comanda_id != None and adicionais1 == None: ##add novo suco em comanda existente
        comanda_atual = comanda_id
        total_pedido = pedido_suco.preco
        novo_item_suco = itemsuco(suco_item=pedido_suco, total=total_pedido)
        novo_item_suco.save()
        comanda_atual.total = comanda_atual.total + total_pedido
        comanda_atual.save()
        comanda_atual.sucos.add(novo_item_suco,)
        comanda_atual.save()
        mixs1 = comanda_atual.mixs.all()
        acais1 = comanda_atual.acais.all()
        casadinhos1 = comanda_atual.casadinhos.all()
        cremes1 = comanda_atual.cremes.all()
        produtos1 = comanda_atual.produtos.all()
        sorvetes1 = comanda_atual.sorvetes.all()
        mshakes1 = comanda_atual.mshakes.all()
        petits1 = comanda_atual.petits.all()
        fondues1 = comanda_atual.fondues.all()
        sucos1 = comanda_atual.sucos.all()
        comanda_id = comanda_atual.id
        return render(request, 'finalizar.html', {'title':'Fechamento', 'sucos1':sucos1, 'fondues1':fondues1, 'petits1':petits1, 'mshakes1':mshakes1, 'sorvetes1':sorvetes1, 'acais1':acais1, 'mixs1':mixs1, 'casadinhos1':casadinhos1, 'cremes1':cremes1, 'produtos1':produtos1, 'comanda_id':comanda_id})
    if pedido_produto != None and comanda_id != None and adicionais1 == None: ##add novo produto em comanda existente
        comanda_atual = comanda_id
        total_pedido = pedido_produto.preco
        novo_item_prod = itemproduto(produto_item=pedido_produto, total=total_pedido)
        novo_item_prod.save()
        comanda_atual.total = comanda_atual.total + total_pedido
        comanda_atual.save()
        comanda_atual.produtos.add(novo_item_prod,)
        comanda_atual.save()
        mixs1 = comanda_atual.mixs.all()
        acais1 = comanda_atual.acais.all()
        casadinhos1 = comanda_atual.casadinhos.all()
        cremes1 = comanda_atual.cremes.all()
        produtos1 = comanda_atual.produtos.all()
        sorvetes1 = comanda_atual.sorvetes.all()
        mshakes1 = comanda_atual.mshakes.all()
        petits1 = comanda_atual.petits.all()
        fondues1 = comanda_atual.fondues.all()
        sucos1 = comanda_atual.sucos.all()
        comanda_id = comanda_atual.id
        return render(request, 'finalizar.html', {'title':'Fechamento', 'sucos1':sucos1, 'fondues1':fondues1, 'petits1':petits1, 'mshakes1':mshakes1, 'sorvetes1':sorvetes1, 'acais1':acais1, 'mixs1':mixs1, 'casadinhos1':casadinhos1, 'cremes1':cremes1, 'produtos1':produtos1, 'comanda_id':comanda_id})
    return render(request, 'finalizar.html',{'title':'Fechamento','comanda_id':comanda_id})

def metodo(request):
    comanda_id = request.GET.get('comanda_id')
    comanda_atual = comanda.objects.filter(id=comanda_id).get()
    Epson = printer.Usb(0x04b8,0x0202)
    acais1 = comanda_atual.acais.all()
    mixs1 = comanda_atual.mixs.all()
    casadinhos1 = comanda_atual.casadinhos.all()
    produtos1 = comanda_atual.produtos.all()
    cremes1 = comanda_atual.cremes.all()
    sorvetes1 = comanda_atual.sorvetes.all()
    mshakes1 = comanda_atual.mshakes.all()
    petits1 = comanda_atual.petits.all()
    fondues1 = comanda_atual.fondues.all()
    
    Epson.text("Comanda N: " + str(comanda_atual.id))
    Epson.text('\n')
    Epson.text('\n')
    Epson.text('------------------------------------------------\n')
    for acais in acais1:
        Epson.text("Acai : " + str(acais.acai_item.nome))
        Epson.text('\n')
        Epson.text('\n')
        Epson.text("Tamanho : " + str(acais.acai_item.tamanho))
        Epson.text('\n')
        Epson.text('\n')
        adds = acais.adicionais.all()
        if adds != None:
            Epson.text('Adicionais:')
            Epson.text('\n')
            for adicionais in adds:
                Epson.text("   - " + str(adicionais))
                Epson.text('\n')
            Epson.text('------------------------------------------------\n')
            Epson.text('\n')
            Epson.text('\n')
    for mixs in mixs1:
        Epson.text("Mix : " + str(mixs.mix_item.nome))
        Epson.text('\n')
        Epson.text('\n')
        Epson.text("Tamanho : " + str(mixs.mix_item.tamanho))
        Epson.text('\n')
        Epson.text('\n')
        adds = mixs.adicionais.all()
        if adds != None:
            Epson.text('Adicionais:')
            Epson.text('\n')
            for adicionais in adds:
                Epson.text("   - " + str(adicionais))
                Epson.text('\n')
            Epson.text('------------------------------------------------\n')
            Epson.text('\n')
            Epson.text('\n')
    for casadinhos in casadinhos1:
        Epson.text("Mix : " + str(casadinhos.casadinho_item.nome))
        Epson.text('\n')
        Epson.text('\n')
        Epson.text("Tamanho : " + str(casadinhos.casadinho_item.tamanho))
        Epson.text('\n')
        Epson.text('\n')
        adds = casadinhos.adicionais.all()
        if adds != None:
            Epson.text('Adicionais:')
            Epson.text('\n')
            for adicionais in adds:
                Epson.text("   - " + str(adicionais))
                Epson.text('\n')
            Epson.text('------------------------------------------------\n')
            Epson.text('\n')
            Epson.text('\n')
    Epson.cut()
    
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
def desconto(request):
    comanda_id = request.GET.get('comanda_id')
    comanda_atual = comanda.objects.filter(id=comanda_id).get()
    if request.method == 'POST':
        comanda_id = request.POST.get('comanda_id')
        comanda_atual = comanda.objects.filter(id=comanda_id).get()
        desc = request.POST.get('desc')
        total_desconto = comanda_atual.total - Decimal(desc)
        comanda_atual.total = total_desconto
        comanda_atual.save()
        return render(request, 'metodo.html', {'title':'Metodo de pagamento', 'comanda_atual':comanda_atual})
    return render(request, 'desconto.html',{'title':'Desconto', 'comanda_atual':comanda_atual})