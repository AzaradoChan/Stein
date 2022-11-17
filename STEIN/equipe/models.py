from django.contrib.auth.models import User
from django.db import models as m
from django.utils import timezone
from django.core.exceptions import ValidationError

from colorfield.fields import ColorField

# Create your models here.
class Setor(m.Model):
    nome = m.CharField(max_length=50, unique=True)
    descricao = m.CharField(max_length=150, verbose_name='Descrição', blank=True, null=True)
    cor = ColorField(default='#808080')

    def __str__(self):
        return f'{self.nome}'

class Cargo(m.Model):
    setor = m.ForeignKey(Setor, on_delete=m.PROTECT, verbose_name='Setor')
    nome = m.CharField(max_length=50, unique=True)
    descricao = m.CharField(max_length=150, verbose_name='Descrição', blank=True, null=True)
    salario = m.DecimalField(max_digits=8, decimal_places=2, verbose_name='Salário')
    administrador = m.BooleanField(default=False)

    def __str__(self):
        return f'{self.nome} - {self.setor.nome} - R$ {self.salario}'


class Funcionario(m.Model):
    def validate_cpf(value):
        if len(value) < 14:
            raise ValidationError('CPF inválido.', code='cpfInválida')
    def validate_ctps(value):
        if len(value) < 11:
            raise ValidationError('CTPS inválida.', code='ctpsInválida')

    primeiro_nome = m.CharField(max_length=20, verbose_name='Primeiro Nome')
    segundo_nome = m.CharField(max_length=80, verbose_name='Sobrenome')
    cpf = m.CharField(max_length=14, unique=True, validators=[validate_cpf])
    ctps = m.CharField(max_length=14, unique=True, validators=[validate_ctps])
    dataNascimento = m.DateField(verbose_name='Data de Nascimento', default='01/01/2000')
    email = m.EmailField(blank=True)
    tel = m.CharField(max_length=15, verbose_name='Telefone', help_text='Com DDD.')
    rua = m.CharField(max_length=30, verbose_name='Rua ou Avenida')
    numero = m.IntegerField(verbose_name='Número')
    bairro = m.CharField(max_length=15, verbose_name='Bairro ou Jardim')
    cidade = m.CharField(max_length=30)
    funcao = m.ForeignKey(Cargo, on_delete=m.PROTECT, verbose_name='Função')
    bonusMensal = m.DecimalField(default=0, max_digits=8, decimal_places=2, verbose_name='Bônus Salarial Mensal')
    dataContratacao = m.DateField(default=timezone.now, verbose_name='Data de Contratação')
    observacao = m.CharField(max_length=255, null=True, blank=True, verbose_name='Observação')
    dataDemicao = m.DateField(null=True, blank=True, verbose_name='Data Demissional:')
    demitido = m.BooleanField(default=False, verbose_name='Demitido:')
    salTotal = m.DecimalField(blank=True, null=True, editable=False, decimal_places=2, max_digits=10, verbose_name='Salário Total')
    motivoDemicao = m.CharField(blank=True, null=True, max_length=100, verbose_name='Motivo da Demissão:')
    administrador = m.BooleanField(default=False)
    contaFuncionario = m.ForeignKey(User, null=True, blank=True, on_delete=m.PROTECT)

    def __str__(self):
        return f'{self.primeiro_nome} - {self.cpf} - {self.funcao.nome}'
