from django.shortcuts import render
from pedidos.models import adicional, acai, mix, casadinho

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

def addadicional(request):
    return render(request, 'addadicional.html', {'title':'Add Adicional'})

