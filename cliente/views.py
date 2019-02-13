from django.shortcuts import render

# Create your views here.
def novo_cliente(request):
    return render(request, 'cliente/novo_cliente.html', {'title':'Novo Cliente'})