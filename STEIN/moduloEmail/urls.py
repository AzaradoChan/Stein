# from views import 
from django.urls import path
from .views import enviar_email

urlpatterns = [
    path('', enviar_email, name='enviarCodigoUnicoMail')
]