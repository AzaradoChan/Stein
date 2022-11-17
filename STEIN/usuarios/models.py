from django.db import models as m
from django.contrib.auth.models import User

# Create your models here.
class Perfil(m.Model):
    nome_completo = m.CharField(max_length=50, null=True)
    cpf = m.CharField(max_length=14, null=True)
    telefone = m.CharField(max_length=15, null=True)
    usuario = m.OneToOneField(User, on_delete=m.CASCADE)

    def __str__(self):
        return f'{self.nome_completo} - {self.telefone}'

