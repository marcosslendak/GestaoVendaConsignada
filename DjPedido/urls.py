from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', admin.site.urls),
#    url(r'^$', views.home, name='home'),
    url(r'^relatorio/$', views.relatorio, name='relatorio'),
    url(r'^ report_builder /', include('report_builder.urls')),
    url(r'^listPedidosSolicitacao/', views.listPedidosSolicitacao),
    url(r'^listPedidosDevolucao/', views.listPedidosDevolucao),
    url(r'^listPedidosFechado/', views.listPedidosFechado),



#    url(r'^admin/', include(admin_reports.site.urls)),


#    url(r'^colaborador/', views.cliente, name='colaborador'),
]
