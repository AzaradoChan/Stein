from django.contrib import admin

from .models import Mesa, Comanda, Comanda_Produto

# Register your models here.
admin.site.register(Mesa)
admin.site.register(Comanda)
admin.site.register(Comanda_Produto)