from django.db import models as m

# Create your models here.

class EmailAnonimo(m.Model):
    codigoUnico = m.CharField(max_length=6, unique=True, primary_key=True)
    email = m.EmailField(unique=True)

    def __str__(self):
        return f'{self.email}'
