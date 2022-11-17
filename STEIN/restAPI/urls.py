from django.urls import path, include

from rest_framework.authtoken import views
from .views import FuncionarioViewSet, CargoViewSet, SetorViewSet, UserViewSet
from .views import ProdutoViewSet, TipoProdutoViewSet
from .views import ComandaViewSet, ComandaProdutoViewSet, MesaViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'Users', UserViewSet)

router.register(r'Funcionarios', FuncionarioViewSet)
router.register(r'Cargos', CargoViewSet)
router.register(r'Setores', SetorViewSet)
router.register(r'Produtos', ProdutoViewSet)
router.register(r'TiposDeProduto', TipoProdutoViewSet)

router.register(r'Comanda', ComandaViewSet)
router.register(r'ComandaProduto', ComandaProdutoViewSet)
router.register(r'Mesa', MesaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('verifica-token/', views.obtain_auth_token, name='ver-apiToken'),
]