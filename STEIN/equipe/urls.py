from django.urls import path

from .views import CargoCreate, SetorCreate, FuncionarioCreate
from .views import SetorList, CargoList, FuncionarioList
from .views import SetorUpdate, CargoUpdate, FuncionarioUpdate, FuncionarioDemicao
from .views import SetorDelete, CargoDelete, FuncionarioDelete

urlpatterns = [
    path('cadastrar/setor/', SetorCreate.as_view(), name='cad-setor'),
    path('cadastrar/cargo/', CargoCreate.as_view(), name='cad-cargo'),
    path('cadastrar/funcionario/', FuncionarioCreate.as_view(), name='cad-funcionario'),

    path('listar/setor/', SetorList.as_view(), name='listar-setor'),
    path('listar/cargo/', CargoList.as_view(), name='listar-cargo'),
    path('listar/funcionario/', FuncionarioList.as_view(), name='listar-funcionario'),

    path('editar/setor/<int:pk>/', SetorUpdate.as_view(), name='edit-setor'),
    path('editar/cargo/<int:pk>/', CargoUpdate.as_view(), name='edit-cargo'),
    path('editar/funcionario/<int:pk>/', FuncionarioUpdate.as_view(), name='edit-funcionario'),
    path('demitir/funcionario/<int:pk>/', FuncionarioDemicao.as_view(), name='demitir-funcionario'),

    path('excluir/setor/<int:pk>/', SetorDelete.as_view(), name='del-setor'),
    path('excluir/cargo/<int:pk>/', CargoDelete.as_view(), name='del-cargo'),
    path('excluir/funcioario/<int:pk>/', FuncionarioDelete.as_view(), name='del-funcionario'),
]