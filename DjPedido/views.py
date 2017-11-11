from django.shortcuts import render, render_to_response
#from DjPedido.forms import ColaboradorForm

def home(request):
    return render_to_response('DjPedido/home.html', {})

#def cliente(request):
#    form = ColaboradorForm()
#    context = {'form':form}
#    return render(request, 'DjPedido/colaborador.html', context)

