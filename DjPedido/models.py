from django.db import models
from django.db.models import F
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
#from localflavor.br.forms import BRCPFField, BRZipCodeField, STATE_CHOICES, BRStateChoiceField
from localflavor.br.models import STATE_CHOICES, BRStateField
from phonenumber_field.modelfields import PhoneNumberField
from django.forms import ModelForm
from django.http.response import HttpResponseForbidden
from django.forms.models import BaseModelFormSet

# Create your models here.

#REPORT_BUILDER_MODEL_MANAGER = 'on_site'

SEXO_CHOICES = (
    ('M', u'Masculino'),
    ('F', u'Feminino'),
)

ESTADO_CIVIL_CHOICES = (
    ('S', u'Solteiro'),
    ('C', u'Casado'),
    ('D', u'Divorciado'),
    ('V', u'Viúvo'),
)

class Colaborador(models.Model):

    nome = models.CharField(max_length=60)
    cpf = models.CharField(max_length=11)
#    cpf = BRCPFField(label='CPF')

    dtNascimento = models.DateField(blank=True, null=True, verbose_name='Data de nascimento')
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, default='F')
    estado_civil = models.CharField(max_length=1, choices=ESTADO_CIVIL_CHOICES, default='C', verbose_name='Estado civil')
    email = models.EmailField(blank=True, null=True)
    cep = models.CharField(max_length=8, blank=True, null=True)
#    cep = BRZipCodeField(label='CEP')

    endereco = models.CharField(max_length=60, blank=True, null=True, verbose_name='Endereço')
    nrEndereco = models.CharField(max_length=60, blank=True, null=True, verbose_name='Nº endereço')
    bairro = models.CharField(max_length=60, blank=True, null=True)
    cidade = models.CharField(max_length=60, blank=True, null=True)
    estado = BRStateField(max_length=2, choices=STATE_CHOICES, default='RS')
    nrTelCelular = PhoneNumberField(max_length=11, blank=True, null=True, verbose_name='Nº telefone celular')
    nrTelFixo = PhoneNumberField(max_length=11, blank=True, null=True, verbose_name='Nº telefone fixo')

    class Meta:
        verbose_name_plural = 'Colaboradores'

    def __str__(self):
        return self.nome

class Supervisor(models.Model):
    idColaborador = models.ForeignKey(Colaborador, verbose_name='Supervisor')
    comissao = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Comissão')

    class Meta:
        verbose_name_plural = 'Supervisores'

    def __str__(self):
        return self.idColaborador.nome


class Vendedor(models.Model):
    idColaborador = models.ForeignKey(Colaborador, verbose_name='Vendedor')
    comissao = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Comissão')

    class Meta:
        verbose_name_plural = 'Vendedores'

    def __str__(self):
        return self.idColaborador.nome


class Item(models.Model):
#    report_builder_model_manager = 'on_site'
    REPORT_BUILDER_INCLUDE = []
    descricao = models.CharField(max_length=60, verbose_name='Descrição')
    ean = models.CharField(max_length=13, verbose_name='EAN')
    precoCusto = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Preço custo')
    preco = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Preço')
    estoqueAtual = models.IntegerField(default=1, blank=False, verbose_name='Estoque atual')

    class Meta:
        verbose_name_plural = 'Itens'

    def __str__(self):
        return self.descricao


class Pedido(models.Model):
    idSupervisor = models.ForeignKey(Supervisor, verbose_name='Supervisor')
    idVendedor = models.ForeignKey(Vendedor, verbose_name='Vendedor')
    dtPedido = models.DateField(auto_now_add=True, verbose_name='Data do pedido')
    solicitando = models.BooleanField(default=True, verbose_name='Pedido aberto')
    fechado = models.BooleanField(default=False, verbose_name='Fechar o pedido')
    dtFechamento = models.DateField(blank=True, null=True, verbose_name='Data do fechamento')
    informacoes = models.TextField(blank=True, null=True, verbose_name='Informações')

    class Meta:
        ordering = ['idSupervisor', 'idVendedor', 'dtPedido']

    def __str__(self):
        return self.informacoes

#        return str(self.dtPedido)
#        return '%s - %s' % (self.dtPedido, self.descricao)


class ItensPedido(models.Model):
    idPedido = models.ForeignKey(Pedido)
    idItem = models.ForeignKey(Item)
    qtdSolicitada = models.IntegerField(default=1, blank=False, verbose_name='Quantidade solicitada')
    qtdDevolvida = models.IntegerField(blank=True, null=True, verbose_name='Quantidade devolvida')
    precoUnitario = models.DecimalField(max_digits=8, decimal_places=2, blank=True, verbose_name='Preço unitário')
#    vlrDescontoUnitario = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True, verbose_name='Valor desconto unitário')


    def __init__(self, *args, **kwargs):
        super(ItensPedido, self).__init__(*args, **kwargs)
        self.set_precoUnitario()

    def save(self, *args, **kwargs):
        self.set_precoUnitario()
        if self.pk is None or self.qtdDevolvida > 0:
            if self.idItem and self.qtdSolicitada > 0:
                Item.objects.filter(id=self.idItem_id).update(
                    estoqueAtual = F('estoqueAtual') - self.qtdSolicitada)
            super(ItensPedido, self).save(*args, **kwargs)
        else:
#            raise Exception('Alteração não permitida.')
#            return HttpResponseForbidden('Alteração não permitida.')
            return 'Alteração não permitida.'

    def delete(self, using=None, keep_parents=False):
        Item.objects.filter(id=self.idItem_id).update(
            estoqueAtual = F('estoqueAtual') + self.qtdSolicitada)
        super(ItensPedido, self).delete()

    def set_precoUnitario(self):
        if self.idItem_id and not self.precoUnitario:
            self.precoUnitario = self.idItem.preco


class PedidoSolicitacaoManager(models.Manager):
    def get_queryset(self):
        return super(PedidoSolicitacaoManager, self).get_queryset().filter(solicitando = True, fechado = False)

class PedidoSolicitacao(Pedido):
    objects = PedidoSolicitacaoManager()
    class Meta:
        verbose_name_plural = 'Solicitação'
        proxy = True


class PedidoDevolucaoManager(models.Manager):
    def get_queryset(self):
        return super(PedidoDevolucaoManager, self).get_queryset().filter(solicitando = False, fechado = False)

class PedidoDevolucao(Pedido):
    objects = PedidoDevolucaoManager()
    class Meta:
        verbose_name_plural = 'Devolução'
        proxy = True



#class Devolucao(BaseModelFormSet):
#    def __init__(self, *args, **kwargs):
#        self.queryset = Pedido.objects.filter(dtFechamento__isnull = True, ativo = True)
#       super(Devolucao, self).__init__(*args, **kwargs)

#class ItensDevolucao(ItensPedido):
#    pass



#    def set_estoque(self):
#        if self.idItem and self.qtdSolicitada > 0:
#            item = Item.objects.get(id=self.idItem_id)
#            #if self._state.adding:
#            item.estoqueAtual = int(self.idItem.estoqueAtual) - int(self.qtdSolicitada)
#            item.save()
##            Item.objects.filter(id=self.idItem_id).update(
##                estoqueAtual = F('estoqueAtual') - self.qtdSolicitada)





#    vlrTotal = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Valor total')


#    def save_model(self, request, obj, form, change):
#        # don't overwrite manually set slug
#        if form.cleaned_data['slug'] == "":
#            obj.slug = slugify(form.cleaned_data['brand']) + "-" + slugify(form.cleaned_data['name'])
#        obj.save()

#    def clean_descricao(self):



#    def getvlrUnitario(self):
#        return self.Item.vlrUnitario


#dispatch.Signal


#@receiver(m2m_changed, sender=ItensPedido.idItem)
#def ItensPedido_idItem_changed(sender, **kwargs):
#    vlrUnitario = kwargs.pop('vlrUnitario', None)


        #def ItensPedido_vlrUnitario(sender, instance, **kwargs):
#    if not instance.vlrUnitario and instance.Item and instance.Item.vlrUnitario:
#        instance.vlrUnitario = instance.Item.vlrUnitario
#        instance.save()
#    return True
#
#models.signals.post_save.connect(ItensPedido_vlrUnitario, sender=ItensPedido, dispatch_uid="vlrUnitario_post_save", weak=False)





# https://www.webforefront.com/django/modelmethodsandmetaoptions.html
# Listing 7-17. Django model with custom method
