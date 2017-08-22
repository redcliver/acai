from django.shortcuts import render
from pedidos.models import adicional, acai

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

def addmix(request):
    return render(request, 'addmix.html', {'title':'Add Mix'})

def addadicional(request):
    return render(request, 'addadicional.html', {'title':'Add Adicional'})

