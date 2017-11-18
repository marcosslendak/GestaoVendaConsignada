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


def listPedidosSolicitacao(request):
    itensPedidosSolicitacao = ItensPedido.objects.select_related('idPedido').filter(idPedido__solicitando=True, idPedido__fechado=False).order_by(
        'idPedido__idSupervisor',
        'idPedido__idVendedor',
        'idPedido__dtPedido',
        'idPedido')
    return render(request, 'DjPedido/listPedidosSolicitacao.html', {'itensPedidosSolicitacao': itensPedidosSolicitacao})


def listPedidosDevolucao(request):
    itensPedidosDevolucao = ItensPedido.objects.select_related('idPedido').filter(idPedido__solicitando=False, idPedido__fechado=False).order_by(
        'idPedido__idSupervisor',
        'idPedido__idVendedor',
        'idPedido__dtPedido',
        'idPedido')
    return render(request, 'DjPedido/listPedidosDevolucao.html', {'itensPedidosDevolucao': itensPedidosDevolucao})


def listPedidosFechado(request):
    itensPedidosFechado = ItensPedido.objects.select_related('idPedido').filter(idPedido__solicitando=False, idPedido__fechado=True).order_by(
        'idPedido__idSupervisor',
        'idPedido__idVendedor',
        'idPedido__dtPedido',
        'idPedido')
    return render(request, 'DjPedido/listPedidosFechado.html', {'itensPedidosFechado': itensPedidosFechado})


def informacoes(request):
    return render(request, 'DjPedido/informacoes.html', {})
