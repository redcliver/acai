from django.shortcuts import render

# Create your views here.
def pedidos(request):
    if request.method == 'GET' and request.GET.get('pedido') != None:
        pedido1 = request.GET.get('pedido')
        if pedido1 == 'acai':
            return render(request, 'acai.html', {'title':'Acai'})
        if pedido1 == 'mix':
            return render(request, 'mix.html', {'title':'Mix'})
        if pedido1 == 'casadinho':
            return render(request, 'casadinho.html', {'title':'Casadinho'})
        return render(request, 'pedidos.html', {'title':'Pedidos'})
    return render(request, 'pedidos.html', {'title':'Pedidos'})