from ajax_select.admin import AjaxSelectAdmin
from ajax_select.helpers import make_ajax_form
from django.contrib import admin
from DjPedido.models import Item, Pedido, ItensPedido, Colaborador, Supervisor, Vendedor, PedidoSolicitacao,  PedidoDevolucao
from django.utils.safestring import mark_safe
from localflavor.br.forms import BRCPFField
from django.http import HttpResponse, HttpResponseRedirect
    #, BRZipCodeField, STATE_CHOICES, BRStateChoiceField

# Register your models here.

#def pdf_version(modeladmin, request, queryset):
#    url = '/your_pdf_url/?pks=' + ','.join([q.pk for q in queryset])
#    HttpResponseRedirect(url)

class ColaboradorAdmin(admin.ModelAdmin):
    model = Colaborador
    fieldsets = [
        ['Informações pessoais', {
            'fields': ['nome',('cpf', 'dtNascimento'), ('sexo', 'estado_civil'), 'email']
        }],
        ['Endereço', {
            'fields': ['cep', ('endereco', 'nrEndereco'), 'bairro', ('cidade', 'estado')],
        }],
    ]

    list_display = ['nome','cpf', 'dtNascimento', 'sexo', 'estado_civil', 'email', 'cep', 'endereco', 'nrEndereco',
                    'bairro', 'cidade', 'estado', 'nrTelCelular', 'nrTelFixo']
    list_filter = ['sexo', 'estado_civil']
    search_fields = ['nome']
#    actions = [pdf_version]
admin.site.register(Colaborador, ColaboradorAdmin)


class SupervisorAdmin(admin.ModelAdmin):
    model = Supervisor
    list_display = ['idColaborador', 'comissao']
    search_fields = ['idColaborador']
admin.site.register(Supervisor, SupervisorAdmin)


class VendedorAdmin(admin.ModelAdmin):
    model = Vendedor
    list_display = ['idColaborador', 'comissao']
    search_fields = ['idColaborador']
admin.site.register(Vendedor, VendedorAdmin)

#class ItemAdmin(admin.ModelAdmin):
class ItemAdmin(AjaxSelectAdmin):
    model = Item
    list_display = ['descricao', 'ean', 'precoCusto', 'preco', 'estoqueAtual']
    search_fields = ['descricao', 'ean']
#    form = make_ajax_form(Item, {'descricao':'item'})
admin.site.register(Item, ItemAdmin)

class ItensPedidoSolicitacaoAdmin(admin.TabularInline):
    model = ItensPedido
    can_delete = True
    extra = 1
    readonly_fields = ['precoUnitario']
    fields = ['idItem', 'qtdSolicitada', 'precoUnitario']
    list_display = ['idItem', 'qtdSolicitada', 'precoUnitario']


class PedidoSolicitacaoAdmin(admin.ModelAdmin):
    model = Pedido
    fields = ['idSupervisor', 'idVendedor', 'solicitando', 'informacoes']
    list_display = ['idSupervisor', 'idVendedor', 'dtPedido', 'solicitando', 'informacoes']
    list_filter = ['dtPedido']
    search_fields = ['idSupervisor', 'idVendedor', 'dtPedido']
    inlines = [ItensPedidoSolicitacaoAdmin]
admin.site.register(PedidoSolicitacao, PedidoSolicitacaoAdmin)


class ItensPedidoDevolucaoAdmin(admin.TabularInline):
    model = ItensPedido
    can_delete = False
    #extra = 1
    readonly_fields = ['qtdSolicitada', 'precoUnitario']
    fields = ['idItem', 'qtdSolicitada', 'qtdDevolvida', 'precoUnitario']
    list_display = ['idItem', 'qtdSolicitada', 'qtdDevolvida', 'precoUnitario']

    def has_add_permission(self, request, obj=None):
        return False

#    def has_delete_permission(self, request, obj=None):
#        return False


class PedidoDevolucaoAdmin(admin.ModelAdmin):
    model = Pedido
    readonly_fields = ['idSupervisor', 'idVendedor', 'dtPedido', 'informacoes']
    fields = ['idSupervisor', 'idVendedor', 'dtPedido', 'fechado', 'informacoes']
    list_display = ['idSupervisor', 'idVendedor', 'dtPedido', 'fechado', 'informacoes']
    list_filter = ['dtPedido']
    search_fields = ['idSupervisor', 'idVendedor']
    inlines = [ItensPedidoDevolucaoAdmin]

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(PedidoDevolucao, PedidoDevolucaoAdmin)





####################
#proxy = True
# PedidoEntregue
# ItensPedidoEntregue

# PedidoDevolvido
# ItensPedidoDevolvido

#####################

####

##https://stackoverflow.com/questions/12790220/why-cant-i-register-multiple-django-modeladmin-with-same-model?rq=1

####

#class PostAdmin(admin.ModelAdmin):
#    list_display = ('title', 'pubdate','user')

#class MyPosts(Post):
#    class Meta:
#        proxy = True

#class MyPostAdmin(PostAdmin):
#    def get_queryset(self, request):
#        return self.model.objects.filter(user = request.user)

#admin.site.register(Post, PostAdmin)
#admin.site.register(MyPost, MyPostAdmin)

#####################

#class ItensDevolucaoAdmin(ItensPedidoAdmin):
#    model = ItensPedido
#    can_delete = False
##    extra = 1
#    readonly_fields = ['qtdSolicitada', 'precoUnitario']
#    fields = ['idItem', 'qtdSolicitada', 'precoUnitario']
#    list_display = ['idItem', 'qtdSolicitada', 'precoUnitario']

#class DevolucaoAdmin(PedidoAdmin):
#    model = Pedido
#    fields = ['idSupervisor', 'idVendedor', 'descricao']
#    list_display = ['idSupervisor', 'idVendedor', 'descricao', 'dtPedido']
#    list_filter = ['dtPedido']
#    search_fields = ['idSupervisor', 'idVendedor']
#    inlines = [ItensDevolucaoAdmin]
#admin.site.register(Devolucao, DevolucaoAdmin)
