from django.db import models as m
from django.utils import timezone

# Create your models here.
class TipoProduto(m.Model):
    tipo = m.CharField(max_length=50, help_text='EX: Suco, Lanche, ...', unique=True)

    def __str__(self):
        return f'{self.tipo}'

class Produto(m.Model):
    tipoProduto = m.ForeignKey(TipoProduto, on_delete=m.PROTECT, verbose_name='Tipo do Produto')
    nome = m.CharField(max_length=60, unique=True)
    preco = m.DecimalField(max_digits=8, decimal_places=2)
    descricao = m.CharField(max_length=150, null=True, blank=True, verbose_name='Descrição')
    dataAdicao = m.DateField(editable=False, default=timezone.now)
    vendendo = m.BooleanField(default=True)
    imagem = m.ImageField(upload_to='images/produtos', null=True)

    def __str__(self):
        return f'{self.nome} - {self.tipoProduto.tipo} - R$ {self.preco}'

