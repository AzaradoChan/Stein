from django.urls import path
from django.contrib.auth import views as auth_views
from .views import UsuarioCreate, PerfilUpdate

urlpatterns = [
    #path('', view, name='')
    path('entrar/', auth_views.LoginView.as_view(
        template_name='usuarios/login.html'
        ), name='entrar'),
    
    path('sair/', auth_views.LogoutView.as_view(), name='sair'),
    path('registrar/usuario', UsuarioCreate.as_view(), name='registrar-usuario'),
    path('atualizar/usuario', PerfilUpdate.as_view(), name='atualizar-usuario')
]