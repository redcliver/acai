from django.shortcuts import render

# Create your views here.
def outros(request):
    return render(request, 'outros.html', {'title':'Outros'})

def addacai(request):
    return render(request, 'addacai.html', {'title':'Add Açaí'})

def addmix(request):
    return render(request, 'addmix.html', {'title':'Add Mix'})

def addadicional(request):
    return render(request, 'addadicional.html', {'title':'Add Adicional'})

