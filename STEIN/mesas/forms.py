from unicodedata import decimal
from django import forms as f

from mesas.models import Comanda, Comanda_Produto


class ComandaForm(f.ModelForm):
    class Meta:
        model = Comanda

        fields = [
            'nmrMesa',
            'funcionario',
            'produtos',
            'observacao',
        ]

        exclude = [
            'encerrada',
            'dataHoraEncerrada'
        ]

        