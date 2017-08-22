from django.shortcuts import render
from caixa.models import caixa

# Create your views here.
def caixa(request):
    caixa_atual = caixa.objects.latest('id')
    return render(request, 'caixa.html', {'title':'Caixa', 'caixa_atual':caixa_atual})