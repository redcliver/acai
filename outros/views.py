from django.shortcuts import render
from pedidos.models import produto , sorvete, adicional, acai, mix, casadinho, creme

# Create your views here.
def outros(request):
    return render(request, 'outros.html', {'title':'Outros'})

def addacai(request):
    adicionais = adicional.objects.all()
    if request.method == 'POST':
        acai_nome = request.POST.get('nome')
        acai_tamanho = request.POST.get('tamanho')
        acai_img = request.POST.get('img')
        acai_preco = request.POST.get('preco')
        acai_add = request.POST.getlist('adicional')
        novo_acai = acai(nome=acai_nome, tamanho=acai_tamanho, img=acai_img, preco=acai_preco)
        novo_acai.save()
        msg = "Açaí salvo com sucesso!"
        return render(request, 'home/home.html',{'title':'Home', 'msg':msg})
    return render(request, 'addacai.html', {'title':'Add Açaí', 'adicionais':adicionais})
def addcasadinho(request):
    adicionais = adicional.objects.all()
    if request.method == 'POST':
        casadinho_nome = request.POST.get('nome')
        casadinho_tamanho = request.POST.get('tamanho')
        casadinho_img = request.POST.get('img')
        casadinho_preco = request.POST.get('preco')
        casadinho_add = request.POST.getlist('adicional')
        novo_casadinho = casadinho(nome=casadinho_nome, tamanho=casadinho_tamanho, img=casadinho_img, preco=casadinho_preco)
        novo_casadinho.save()
        msg = "Mix salvo com sucesso!"
        return render(request, 'home/home.html',{'title':'Home', 'msg':msg})
    return render(request, 'addmix.html', {'title':'Add Mix'})
def addmix(request):
    adicionais = adicional.objects.all()
    if request.method == 'POST':
        mix_nome = request.POST.get('nome')
        mix_tamanho = request.POST.get('tamanho')
        mix_img = request.POST.get('img')
        mix_preco = request.POST.get('preco')
        mix_add = request.POST.getlist('adicional')
        novo_mix = mix(nome=mix_nome, tamanho=mix_tamanho, img=mix_img, preco=mix_preco)
        novo_mix.save()
        msg = "Mix salvo com sucesso!"
        return render(request, 'home/home.html',{'title':'Home', 'msg':msg})
    return render(request, 'addmix.html', {'title':'Add Mix'})
def addcreme(request):
    adicionais = adicional.objects.all()
    if request.method == 'POST':
        creme_nome = request.POST.get('nome')
        creme_tamanho = request.POST.get('tamanho')
        creme_img = request.POST.get('img')
        creme_preco = request.POST.get('preco')
        creme_add = request.POST.getlist('adicional')
        novo_creme = creme(nome=creme_nome, tamanho=creme_tamanho, img=creme_img, preco=creme_preco)
        novo_creme.save()
        msg = "Creme salvo com sucesso!"
        return render(request, 'home/home.html',{'title':'Home', 'msg':msg})
    return render(request, 'addcreme.html', {'title':'Add Creme', 'adicionais':adicionais})
def addproduto(request):
    if request.method == 'POST':
        prod_nome = request.POST.get('nome')
        prod_img = request.POST.get('img')
        prod_preco = request.POST.get('preco')
        novo_prod = produto(nome=prod_nome, img=prod_img, preco=prod_preco)
        novo_prod.save()
        msg = "Produto salvo com sucesso!"
        return render(request, 'home/home.html',{'title':'Home', 'msg':msg})
    return render(request, 'addproduto.html', {'title':'Add Produto'})
def addsorvete(request):
    if request.method == 'POST':
        sorv_nome = request.POST.get('nome')
        sorv_img = request.POST.get('img')
        sorv_preco = request.POST.get('preco')
        novo_sorv = sorvete(nome=sorv_nome, img=sorv_nome, preco=sorv_preco)
        novo_sorv.save()
        msg = "Sorvete salvo com sucesso!"
        return render(request, 'home/home.html',{'title':'Home', 'msg':msg})
    return render(request, 'addsorvete.html', {'title':'Add Sorvete'})


def addadicional(request):
    return render(request, 'addadicional.html', {'title':'Add Adicional'})

