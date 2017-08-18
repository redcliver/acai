from django.shortcuts import render

# Create your views here.
def pedidos(request):
    if request.method == 'GET' and request.GET.get('pedido') != None:
        pedido1 = request.GET.get('pedido')
        if pedido1 == 'acai':
            return render(request, 'acai.html', {'title':'Acai'})
        if pedido1 == 'casadinho':
            return render(request, 'casadinho.html', {'title':'Casadinho'})
        if pedido1 == 'mix':
            return render(request, 'mix.html', {'title':'Mix'})
        if pedido1 == 'acaienergy':
            return render(request, 'acaienergy.html', {'title':'acaienergy'})
        if pedido1 == 'acaicreme':
            return render(request, 'acaicreme.html', {'title':'acaicreme'})
        if pedido1 == 'sorvete':
            return render(request, 'sorvete.html', {'title':'sorvete'})
        if pedido1 == 'milkshake':
            return render(request, 'milkshake.html', {'title':'milkshake'})
        if pedido1 == 'petit':
            return render(request, 'petit.html', {'title':'petit'})
        if pedido1 == 'fondue':
            return render(request, 'fondue.html', {'title':'fondue'})
        if pedido1 == 'sucos':
            return render(request, 'sucos.html', {'title':'sucos'})
        if pedido1 == 'produtos':
            return render(request, 'produtos.html', {'title':'produtos'})
        return render(request, 'pedidos.html', {'title':'Pedidos'})
    return render(request, 'pedidos.html', {'title':'Pedidos'})