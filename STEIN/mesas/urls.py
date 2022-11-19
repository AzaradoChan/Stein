from unicodedata import name
from django.urls import path

from .views import ComandaCreate, criarComanda
from .views import atualizarProdutoComanda, atualizarPedido, atualizarValorPagoComanda, chamarGarcom
from .views import ComandaList, ComandaProdutoList, ComandaRetaguardaList, VerComandaAnonList, ComandaSimplesList
from .views import ComandaDelete

urlpatterns = [
    path('fazer-pedido/', ComandaCreate.as_view(), name='cad-comanda'),
    path('fazer-pedido/criarcomanda/', criarComanda, name='criarpedidoAjax'),

    path('listar/comandas/gerenciamento',
         ComandaList.as_view(), name='listar-comanda'),
    path('listar/comandas/', ComandaSimplesList.as_view(), name='gerencia-comanda'),
    path('listar/comandas/retaguarda/',
         ComandaRetaguardaList.as_view(), name='listar-retaguarda'),

    path('editar/pedido/<comanda_id>/produtos/',
         ComandaProdutoList.as_view(), name='edit-comProd'),

    path('atualizar/comanda/produtos/', atualizarProdutoComanda,
         name='atualizarpedidocomandaAjax'),
    path('atualizar/comanda/pedidos/',
         atualizarPedido, name='atualizarPedidoAjax'),
    path('atualizar/comanda/pago/', atualizarValorPagoComanda,
         name='atualizarPagComanda'),

    path('deletar/comanda/<int:pk>/', ComandaDelete.as_view(), name='del-comanda'),

    path('ver/pedido/auto-autendimento/<codigo_anon>',
         VerComandaAnonList.as_view(), name='ver-comandaAnon'),

    path('pedido/anonimo/chamar-garcom/', chamarGarcom, name='chamar-garcom'),
]
