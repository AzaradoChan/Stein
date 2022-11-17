from django.urls import path
from .views import Modelo, Inicio, Formulario, Agradecimento

urlpatterns = [
    path('modelo/', Modelo.as_view(), name='model'),
    path('', Inicio.as_view(), name='index'),
    path('formulario/', Formulario.as_view(), name='form'),
    path('agradecimento/', Agradecimento.as_view(), name='agradecimento')
]