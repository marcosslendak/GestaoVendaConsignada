from django import forms
from localflavor.br.forms import BRCPFField, STATE_CHOICES, BRCNPJField
from phonenumber_field.formfields import PhoneNumberField
from input_mask.contrib.localflavor.br.widgets import BRPhoneNumberInput
from DjPedido.models import Pedido, ItensPedido

#class ColaboradorForm(forms.Form):
#
#    nome = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_lenght=60)),
#        label='Nome', error_messages={'invalid': 'Nome deve conter apenas letras.'})
#
#    cpf = BRCPFField(required=True)
#    dtNascimento = forms.DateField(widget=forms.DateInput(format='%d/%m/%Y'),required=False)
#
#    sexo = forms.CharField(max_length=1)
#    estado_civil = forms.CharField(max_length=1)
#    email = forms.EmailField(required=False)
#    cep = forms.CharField(max_length=8, required=False)
#
##    cep = BRZipCodeField(label='CEP')
#
#    endereco = forms.CharField(max_length=60, required=False)
#    nrEndereco = forms.CharField(max_length=60, required=False)
#    bairro = forms.CharField(max_length=60, required=False)
#    cidade = forms.CharField(max_length=60, required=False)
#
##    estado = forms.CharField(max_length=2, required=False, choices=STATE_CHOICES)
#
##    nrTelCelular = PhoneNumberField()
##    nrTelFixo = PhoneNumberField()
#
#    nrTelCelular = PhoneNumberField(max_length=11, widget=BRPhoneNumberInput)
#    nrTelFixo = PhoneNumberField(max_length=11, widget=BRPhoneNumberInput)


class DevolucaoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        exclude = ('dtPedido', 'ativo')

    def __init__(self, *args, **kwargs):
       self.queryset = Pedido.objects.filter(dtFechamento__isnull = True, ativo = True)
       super(Pedido, self).__init__(*args, **kwargs)