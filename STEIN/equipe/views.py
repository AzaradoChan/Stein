from django.contrib.auth.models import User, Group

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from django.urls import reverse_lazy

from braces.views import GroupRequiredMixin, StaffuserRequiredMixin
gAdm = [u'Gerência']

from .models import Setor, Cargo, Funcionario

# Create your views here.
class SetorCreate(GroupRequiredMixin, StaffuserRequiredMixin, CreateView):
    login_url = reverse_lazy('entrar')
    group_required = gAdm
    model = Setor
    fields = ['nome', 'descricao', 'cor']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('listar-setor')
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = 'Cadastrar Setores.'
        context['botao_submit']  = 'Cadastrar'

        return context
    
class CargoCreate(GroupRequiredMixin, StaffuserRequiredMixin, CreateView):
    login_url = reverse_lazy('entrar')
    group_required = gAdm
    model = Cargo
    fields = ['setor', 'nome', 'salario', 'descricao', 'administrador']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('listar-cargo')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = 'Cadastrar Cargos.'
        context['botao_submit']  = 'Cadastrar'

        return context

class FuncionarioCreate(GroupRequiredMixin, StaffuserRequiredMixin, CreateView):
    login_url = reverse_lazy('entrar')
    group_required = gAdm
    model = Funcionario
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('listar-funcionario')
    fields = ['primeiro_nome', 'segundo_nome', 'cpf', 'ctps','email', 'dataNascimento', 'tel', 'rua', 'numero', 'bairro', 'cidade', 'funcao', 'bonusMensal', 'dataContratacao', 'observacao', 'administrador']

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = 'Cadastrar Funcionário'
        context['botao_submit']  = 'Cadastrar'
        context['tipoCad'] = 'funcionario'

        return context

    def form_valid(self, form):
        url = super().form_valid(form)
        self.object.salTotal = self.object.funcao.salario + self.object.bonusMensal

        if self.object.funcao.administrador == True:
            self.object.administrador = True
            self.object.save()

        if self.object.email != '':
            if self.object.funcao.administrador or self.object.administrador:
                usuario = User.objects.create_user(
                    username=str(self.object.cpf).replace('.', '').replace('-', ''),
                    password=self.object.dataNascimento.strftime('%d%m%Y'),
                    email=str(self.object.email).lower(),
                    is_staff=True,
                    first_name=str(self.object.primeiro_nome),
                    last_name=str(self.object.segundo_nome)
                )
            else:
                    usuario = User.objects.create_user(
                    username=str(self.object.cpf).replace('.', '').replace('-', ''),
                    password=self.object.dataNascimento.strftime('%d%m%Y'),
                    email=str(self.object.email).lower(),
                    first_name=str(self.object.primeiro_nome),
                    last_name=str(self.object.segundo_nome)
                )
        else:
            if self.object.funcao.administrador or self.object.administrador:
                usuario = User.objects.create_superuser(
                    username=str(self.object.cpf).replace('.', '').replace('-', ''),
                    password=self.object.dataNascimento.strftime('%d%m%Y'),
                    is_staff=True,
                    first_name=str(self.object.primeiro_nome),
                    last_name=str(self.object.segundo_nome)
                )
            else:
                usuario = User.objects.create_user(
                    username=str(self.object.cpf).replace('.', '').replace('-', ''),
                    password=self.object.dataNascimento.strftime('%d%m%Y'),
                    first_name=str(self.object.primeiro_nome),
                    last_name=str(self.object.segundo_nome)
                )
        self.object.contaFuncionario = User.objects.get(username=str(self.object.cpf).replace('.', '').replace('-', ''))
        alteraGrupos(self.object)
        self.object.save()

        return url

class SetorList(GroupRequiredMixin, StaffuserRequiredMixin, ListView):
    login_url = reverse_lazy('entrar')
    group_required = gAdm
    model = Setor
    template_name = 'paginas/listas/setor.html'

class CargoList(GroupRequiredMixin, StaffuserRequiredMixin, ListView):
    login_url = reverse_lazy('entrar')
    group_required = gAdm
    model = Cargo
    template_name = 'paginas/listas/cargo.html'
    paginate_by = 10

    def get_queryset(self):

        filtro = self.request.GET.get('filtro')
        if filtro == None:
            self.cargos = Cargo.objects.all()
        else:
            self.cargos = Cargo.objects.filter(setor=filtro)

        self.setores = Setor.objects.all()

        return self.cargos, self.setores

class FuncionarioList(GroupRequiredMixin, StaffuserRequiredMixin, ListView):
    login_url = reverse_lazy('entrar')
    group_required = gAdm
    model = Funcionario
    template_name = 'paginas/listas/funcionario.html'
    paginate_by = 2

    def get_queryset(self):

        self.cargos = Cargo.objects.all()
        cargo = self.request.GET.get('cargo')
        contract = self.request.GET.get('contract')
        
        if cargo == 'none':
            cargo = None
        if contract == 'none':
            contract = None

        if cargo == None and contract == None:
            self.funcs = Funcionario.objects.all().order_by('demitido', 'primeiro_nome')
        elif cargo != None and contract == None:
            self.funcs = Funcionario.objects.filter(funcao=cargo).order_by('demitido', 'primeiro_nome')
        elif cargo == None and contract != None:
            self.funcs = Funcionario.objects.filter(demitido=contract).order_by('demitido', 'primeiro_nome')
        elif cargo != None and contract != None:
            self.funcs = Funcionario.objects.filter(funcao=cargo).filter(demitido=contract).order_by('demitido', 'primeiro_nome')
        return self.funcs, self.cargos




class SetorUpdate(GroupRequiredMixin, StaffuserRequiredMixin, UpdateView):
    login_url = reverse_lazy('entrar')
    group_required = gAdm
    model = Setor
    template_name = 'paginas/form.html'
    fields = ['nome', 'descricao', 'cor']
    success_url = reverse_lazy('listar-setor')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = 'Editar Setor'
        context['botao_submit'] = 'Atualizar'

        return context

class CargoUpdate(GroupRequiredMixin, StaffuserRequiredMixin, UpdateView):
    login_url = reverse_lazy('entrar')
    group_required = gAdm
    model = Cargo
    template_name = 'paginas/form.html'
    fields = ['setor', 'nome', 'salario', 'descricao', 'administrador']
    success_url = reverse_lazy('listar-cargo')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = 'Editar Cargo'
        context['botao_submit'] = 'Atualizar'

        return context

class FuncionarioUpdate(GroupRequiredMixin, StaffuserRequiredMixin, UpdateView):
    login_url = reverse_lazy('entrar')
    group_required = gAdm
    model = Funcionario
    template_name = 'paginas/form.html'
    fields = ['primeiro_nome', 'segundo_nome', 'cpf', 'ctps', 'email', 'dataNascimento', 'tel', 'rua', 'numero', 'bairro', 'cidade', 'funcao', 'bonusMensal', 'dataContratacao', 'observacao', 'demitido', 'dataDemicao', 'motivoDemicao', 'administrador']
    success_url = reverse_lazy('listar-funcionario')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = 'Editar Funcionario'
        context['botao_submit'] = 'Atualizar'
        context['tipoCad'] = 'funcionario'

        return context
    
    def form_valid(self, form):
        url = super().form_valid(form)

        self.object.salTotal = self.object.funcao.salario + self.object.bonusMensal
        if self.object.funcao.administrador == True:
            self.object.administrador = True
            self.object.save()
        
        if self.object.demitido == False:
            self.object.dataDemicao = None
            conta = User.objects.get(username=str(self.object.cpf).replace('.', '').replace('-', ''))
            conta.is_active = True
            conta.save()
        if self.object.administrador:
            conta = User.objects.get(username=str(self.object.cpf).replace('.', '').replace('-', ''))
            conta.is_staff = True
            conta.save()
        else:
            conta = User.objects.get(username=str(self.object.cpf).replace('.', '').replace('-', ''))
            conta.is_staff = False
            conta.save()
        alteraGrupos(self.object)
        self.object.save()

        return url

class FuncionarioDemicao(GroupRequiredMixin, StaffuserRequiredMixin, UpdateView):
    login_url = reverse_lazy('entrar')
    group_required = gAdm
    model = Funcionario
    template_name = 'paginas/demitir.html'
    success_url = reverse_lazy('listar-funcionario')

    fields = ['demitido', 'dataDemicao', 'motivoDemicao']

    def form_valid(self, form):
        url = super().form_valid(form)
        conta = User.objects.get(username=str(self.object.cpf).replace('.', '').replace('-', ''))
        conta.is_active = False
        conta.save()
        return url


class SetorDelete(GroupRequiredMixin, StaffuserRequiredMixin, DeleteView):
    login_url = reverse_lazy('entrar')
    group_required = gAdm
    model = Setor
    template_name = 'paginas/form-excluir.html'
    success_url = reverse_lazy('listar-setor')


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = 'Deletar Setor'

        return context

class CargoDelete(GroupRequiredMixin, StaffuserRequiredMixin, DeleteView):
    login_url = reverse_lazy('entrar')
    group_required = gAdm
    model = Cargo
    template_name = 'paginas/form-excluir.html'
    success_url = reverse_lazy('listar-cargo')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = 'Deletar Cargo'

        return context

class FuncionarioDelete(GroupRequiredMixin, StaffuserRequiredMixin, DeleteView):
    login_url = reverse_lazy('entrar')
    group_required = gAdm
    model = Funcionario
    template_name = 'paginas/form-excluir.html'
    success_url = reverse_lazy('listar-funcionario')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = 'Deletar Funcionario'

        return context



def alteraGrupos(funcionario):
    funcionario.contaFuncionario.groups.clear()
    
    if funcionario.administrador:
        grupo = Group.objects.get(name='Gerência')
        grupo.user_set.add(funcionario.contaFuncionario)
    
    grupo = Group.objects.get(name=funcionario.funcao.setor.nome)
    grupo.user_set.add(funcionario.contaFuncionario)

    funcionario.save()
