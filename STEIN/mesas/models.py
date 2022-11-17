from email.policy import default
from tkinter import CASCADE
from django.db import models as m
from django.utils import timezone
from django.core.exceptions import ValidationError


from moduloEmail.models import EmailAnonimo
from equipe.models import Funcionario
from estoque.models import Produto

# Create your models here.
class Mesa(m.Model):
    numero = m.IntegerField(verbose_name='Número da Mesa:')
    ocupada = m.BooleanField(default=False, blank=True)
    garcom = m.BooleanField(default=False, blank=True)

    def __str__(self):
        return f'{self.numero}'

class Comanda(m.Model):
    def validate_nmrMesa(value):
        try:
            tam = len(Comanda.objects.exclude(nmrMesa__lt=value).exclude(nmrMesa__gt=value).values())
        except:
            a = 1
        else:
            a = 0

        if tam != 0:
            raise ValidationError('A mesa já está ocupada', code='MesaOcupada')

    nmrMesa = m.ForeignKey(Mesa, on_delete=m.PROTECT, validators=[validate_nmrMesa])
    funcionario = m.ForeignKey(Funcionario, on_delete=m.PROTECT)
    produtos = m.ManyToManyField(Produto, through='Comanda_Produto')
    valorTotal = m.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True, default=0)
    valorPago = m.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True, default=0)
    atualizada = m.DateTimeField(auto_now=True)
    dataHoraCriada = m.DateTimeField(default=timezone.now, editable=False)
    dataCriada = m.DateField(auto_now_add=True, editable=False)
    encerrada = m.BooleanField(default=False)
    dataHoraEncerrada = m.DateTimeField(null=True, blank=True)
    observacao = m.CharField(null=True, blank=True, max_length=255)
    contaAnon = m.ForeignKey(EmailAnonimo, null=True, blank=True, on_delete=m.PROTECT)

    def __str__(self):
        return f'{self.nmrMesa} ({self.funcionario.primeiro_nome}) - {self.dataHoraCriada.date()} {self.dataHoraCriada.time()}'

class Comanda_Produto(m.Model):
    comanda = m.ForeignKey(Comanda, on_delete=m.CASCADE)
    produto = m.ForeignKey(Produto, on_delete=m.PROTECT)
    quantidade = m.IntegerField(default=1)
    quantidadeEntregue = m.IntegerField(default=0)
    horaPedido = m.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.comanda}'