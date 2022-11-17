from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User, Group
from django.urls import reverse_lazy
from .forms import UsuarioForm
from django.shortcuts import get_object_or_404
from .models import Perfil

class UsuarioCreate(CreateView):
    form_class = UsuarioForm
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('entrar')

    def form_valid(self, form):
        grupo = get_object_or_404(Group, name='Docentes')
        
        url = super().form_valid(form)

        self.object.groups.add(grupo)
        self.object.save

        Perfil.objects.create(usuario=self.object)

        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = 'Cadastrar Usuário'
        context['bot1'] = 'Registrar'
        context['icone'] = '<i class="fa fa-user-plus" aria-hidden="true"></i>'

        return context
# Create your views here.

class PerfilUpdate(UpdateView):
    template_name = 'cadastros/form.html'
    model = Perfil
    fields = ['nome_completo', 'cpf', 'telefone']
    success_url = reverse_lazy('inicio')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Perfil, usuario=self.request.user)

        return self.object

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = 'Meus Dados'
        context['bot1'] = 'Atualizar Dados'

        return context
