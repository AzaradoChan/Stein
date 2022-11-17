from django.conf.urls.static import static
from django.urls import path

from .views import TipoProdutoCreate, ProdutoCreate
from .views import TipoProdutolist, ProdutoList
from .views import TipoProdutoUpdate, ProdutoUpdate
from .views import TipoProdutoDelete, ProdutoDelete

urlpatterns = [
    path('cadastrar/tipo-produto/', TipoProdutoCreate.as_view(), name='cad-tProduto'),
    path('cadastrar/produto/', ProdutoCreate.as_view(), name='cad-produto'),

    path('listar/tipo-produto/', TipoProdutolist.as_view(), name='listar-tProduto'),
    path('listar/produto/', ProdutoList.as_view(), name='listar-produto'),

    path('atualizar/tipo-produto/<int:pk>', TipoProdutoUpdate.as_view(), name='edit-tProduto'),
    path('atualizar/produto/<int:pk>', ProdutoUpdate.as_view(), name='edit-produto'),

    path('excluir/tipo-produto/<int:pk>', TipoProdutoDelete.as_view(), name='del-tProduto'),
    path('excluir/produto/<int:pk>', ProdutoDelete.as_view(), name='del-produto'),
]