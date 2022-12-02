from rest_framework import viewsets, permissions

import django.http as http

import json

from django.contrib.auth.models import User
from equipe.models import Funcionario, Cargo, Setor
from estoque.models import TipoProduto, Produto
from mesas.models import Comanda, Comanda_Produto, Mesa

from rest_framework.authentication import TokenAuthentication

from .serializers import UserSerializer
from .serializers import FuncionarioSerializer, SetorSerializer, CargoSerializer
from .serializers import ProdutoSerializer, TipoProdutoSerializer
from .serializers import ComandaSerializer, ComandaProdutoSerializer, MesaSerializer

from mesas.views import AtualizaValTotComanda

# Create your models here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_superuser or self.request.user.is_staff:
            print(self.request)
            return super().get_queryset()
        else:
            return None


class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all().exclude(demitido=True)
    serializer_class = FuncionarioSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_superuser or self.request.user.is_staff or self.request.user.has_perm('equipe.view_funcionario'):
            usuario = self.request.query_params.get('usuario')
            if self.request.query_params.get('usuario') != None:
                retorno = Funcionario.objects.filter(
                    contaFuncionario__username=usuario)
                return retorno
            else:
                return None
        else:
            return None


class CargoViewSet(viewsets.ModelViewSet):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_superuser or self.request.user.is_staff or self.request.user.has_perm('equipe.view_cargo'):
            return super().get_queryset()
        else:
            return None


class SetorViewSet(viewsets.ModelViewSet):
    queryset = Setor.objects.all()
    serializer_class = SetorSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_superuser or self.request.user.is_staff or self.request.user.has_perm('equipe.view_setor'):
            return super().get_queryset()
        else:
            return None


class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_superuser or self.request.user.is_staff or self.request.user.has_perm('estoque.view_produto'):
            idProduto = self.request.query_params.get('id')
            if idProduto is not None:
                return Produto.objects.filter(id=idProduto)
            else:
                return super().get_queryset()
        else:
            return None


class TipoProdutoViewSet(viewsets.ModelViewSet):
    queryset = TipoProduto.objects.all()
    serializer_class = TipoProdutoSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_superuser or self.request.user.is_staff or self.request.user.has_perm('estoque.view_tipoproduto'):
            return super().get_queryset()
        else:
            return None


class ComandaViewSet(viewsets.ModelViewSet):
    queryset = Comanda.objects.all()
    serializer_class = ComandaSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_superuser or self.request.user.is_staff or self.request.user.has_perm('mesas.view_comanda'):
            encerrada = self.request.query_params.get('encerrada')
            idMesa = self.request.query_params.get('idMesa')
            if encerrada is not None and idMesa is None:
                return Comanda.objects.filter(encerrada=encerrada)
            elif encerrada is None and idMesa is not None:
                return Comanda.objects.filter(nmrMesa=idMesa)
            elif encerrada is not None and idMesa is not None:
                return Comanda.objects.filter(encerrada=encerrada, nmrMesa=idMesa)
            else:
                return super().get_queryset()
        else:
            return None

    def create(self, request, *args, **kwargs):
        dados = request.data
        idMesa = dados['idMesa']
        idFuncionario = dados['idFuncionario']
        idFuncionario = str(idFuncionario[63:len(str(idFuncionario))-1])
        produtos = dados['produtos']
        observacao = dados['observacao']
        
        if len(Mesa.objects.filter(id=idMesa, ocupada=True)) == 0:
            if observacao == '':
                comanda = Comanda(nmrMesa_id=idMesa, funcionario_id=idFuncionario)
            else:
                comanda = Comanda(nmrMesa_id=idMesa, funcionario_id=idFuncionario, observacao=observacao)
            comanda.save()

            mesa = Mesa.objects.get(id=idMesa)
            mesa.ocupada = True 
            mesa.save()
            for produto in produtos:
                cp = Comanda_Produto(
                    comanda_id=comanda.pk,
                    produto_id=produto['idProduto'],
                    quantidade=produto['quantidade']
                )
                cp.save()
        elif len(Mesa.objects.filter(id=idMesa, ocupada=True)) != 0:
            comanda = Comanda.objects.get(nmrMesa_id=idMesa, encerrada=False)
            if not observacao == '':
                comanda.observacao=observacao
                comanda.save()

            prodPedidos = Comanda_Produto.objects.filter(comanda_id=comanda.pk)
            for produto in produtos:
                for pproduto in prodPedidos:
                    if str(pproduto.produto.id) == produto['idProduto']:
                        if int(pproduto.quantidade) < produto['quantidade']:
                            pproduto.quantidade = produto['quantidade']
                        elif int(pproduto.quantidade) > produto['quantidade'] and int(pproduto.quantidadeEntregue) > produto['quantidade']:
                            pass
                        pproduto.save()
                    else:
                        cp = Comanda_Produto(
                            comanda_id=comanda.pk,
                            produto_id=produto['idProduto'],
                            quantidade=produto['quantidade']
                        )
                        cp.save()

        AtualizaValTotComanda(comanda)
        return http.HttpResponse('Comanda Criada com Sucesso.', 200)

class ComandaProdutoViewSet(viewsets.ModelViewSet):
    queryset = Comanda_Produto.objects.all()
    serializer_class = ComandaProdutoSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_superuser or self.request.user.is_staff or self.request.user.has_perm('mesas.view_comandaproduto'):
            comanda = self.request.query_params.get('comanda')
            if comanda is not None:
                return Comanda_Produto.objects.filter(comanda=comanda)
            else:
                return super().get_queryset()
        else:
            return None


class MesaViewSet(viewsets.ModelViewSet):
    queryset = Mesa.objects.all()
    serializer_class = MesaSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_superuser or self.request.user.is_staff or self.request.user.has_perm('mesas.view_mesa'):
            ocupada = self.request.query_params.get('ocupada')
            if ocupada is not None:
                return Mesa.objects.filter(ocupada=ocupada)
            else:
                return super().get_queryset()
        else:
            return None
