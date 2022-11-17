from django.contrib import admin
from .models import Setor, Cargo, Funcionario

# Register your models here.
admin.site.register(Setor)
admin.site.register(Cargo)
admin.site.register(Funcionario)