from ajax_select import register, LookupChannel
from DjPedido.models import Item

#@register('item')
#class ItemLookup(LookupChannel):
#    model = Item
#
#    def get_query(self, q, request):
#        return self.model.objects.filter(descricao__icontains=q).order_by('descricao')


