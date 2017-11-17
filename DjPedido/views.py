from django.shortcuts import render, render_to_response
from django.http import HttpResponse
#from DjPedido.forms import ColaboradorForm
from .models import Pedido, PedidoDevolucao, ItensPedido

def home(request):
    return render_to_response('DjPedido/home.html', {})


def relatorio(request):
    return HttpResponse('Funcionou....')

#def cliente(request):
#    form = ColaboradorForm()
#    context = {'form':form}
#    return render(request, 'DjPedido/colaborador.html', context)

def pedidoDevolucoes_list(request):
    #itensPedidoDevolucoes = ItensPedido.objects.select_related('idPedido').prefetch_related('')

#    itensPedidoDevolucoes = ItensPedido.objects.select_related('idPedido').filter(idPedido__solicitando=False, idPedido__fechado=False).order_by(
#    'idPedido__idSupervisor',
#    'idPedido__idVendedor',
#    'idPedido__dtPedido',
#    'idPedido')


    #qtdSolicitada = models.IntegerField(default=1, blank=False, verbose_name='Quantidade solicitada')
    #qtdDevolvida

    #idIte

    itensPedidoDevolucoes = ItensPedido.objects.select_related('idPedido').filter(idPedido__solicitando=False, idPedido__fechado=False).order_by(
        'idPedido__idSupervisor',
        'idPedido__idVendedor',
        'idPedido__dtPedido',
        'idPedido')



    return render(request, 'DjPedido/pdlist.html', {'itensPedidoDevolucoes': itensPedidoDevolucoes})


