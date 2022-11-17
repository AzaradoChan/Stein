from rest_framework import serializers
from django.contrib.auth.models import User

from equipe.models import Funcionario, Cargo, Setor
from estoque.models import Produto, TipoProduto
from mesas.models import Comanda, Comanda_Produto, Mesa

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name', 'is_superuser', 'is_staff', 'is_active']


class FuncionarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Funcionario
        
        fields = '__all__'

class CargoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cargo
        fields = '__all__'

class SetorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Setor
        fields = '__all__'

class ProdutoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'

class TipoProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoProduto
        fields = '__all__'

class ComandaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comanda
        fields = '__all__'

class ComandaProdutoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comanda_Produto
        fields = '__all__'

class MesaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Mesa
        fields = '__all__'