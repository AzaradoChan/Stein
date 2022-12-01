from django.views.generic import TemplateView
import mesas.models as mModels
import estoque.models as eModels
import datetime
import django.http as http

# Create your views here.
class Modelo(TemplateView):
    template_name = 'paginas/modelo.html'

class Inicio(TemplateView):
    template_name = 'paginas/inicio.html'
    def get_context_data(self, **kwargs):
        cont = super().get_context_data(**kwargs)

        # FILTRAR PRODUTOS PEDIDOS DE DIA DE HOJE - 30 DIAS.
        
        return cont

class Formulario(TemplateView):
    template_name = 'paginas/form.html'

class Agradecimento(TemplateView):
    template_name = 'paginas/modelo.html'