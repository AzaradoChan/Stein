from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from braces.views import GroupRequiredMixin, StaffuserRequiredMixin

gAdm = [u'Gerência']
gCAdministrativo = [u'Administração'] + gAdm

from .models import TipoProduto, Produto

from django.urls import reverse_lazy

# Create your views here.
class TipoProdutoCreate(GroupRequiredMixin, StaffuserRequiredMixin, CreateView):
    login_url = reverse_lazy('entrar')
    group_required = gAdm
    model = TipoProduto
    fields = ['tipo']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('listar-tProduto')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = 'Cadastro de Tipos de Produtos.'
        context['botao_submit'] = 'Cadastrar'

        return context

class ProdutoCreate(GroupRequiredMixin, StaffuserRequiredMixin, CreateView):
    login_url = reverse_lazy('entrar')
    group_required = gAdm
    model = Produto
    fields = ['tipoProduto', 'nome', 'preco', 'descricao', 'vendendo', 'imagem']
    template_name = 'paginas/form-upload.html'
    success_url = reverse_lazy('listar-produto')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = 'Cadastro de Produtos'
        context['botao_submit'] = 'Cadastrar'

        return context



class TipoProdutolist(GroupRequiredMixin, ListView):
    login_url = reverse_lazy('entrar')
    group_required = gAdm
    model = TipoProduto
    template_name = 'paginas/listas/tipoProduto.html'

class ProdutoList(ListView):
    model = Produto
    template_name = 'paginas/listas/produto.html'

    def get_queryset(self):
        if self.request.user.is_staff:
            qSet = Produto.objects.all().order_by('-vendendo')
        else:
            qSet = Produto.objects.filter(vendendo=True)
        tProdutos = TipoProduto.objects.all()
        return qSet, tProdutos



class TipoProdutoUpdate(GroupRequiredMixin, StaffuserRequiredMixin, UpdateView):
    login_url = reverse_lazy('entrar')
    group_required = gAdm
    model = TipoProduto
    template_name = 'paginas/form.html'
    fields = ['tipo']
    success_url = reverse_lazy('listar-tProduto')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = 'Atualizar Tipo de Produto'
        context['botao_submit'] = 'Atualizar'

        return context

    def get_queryset(self):
        self.produtos = Produto.objects.all().order_by('vendendo', 'nome')
        return self.produtos

class ProdutoUpdate(GroupRequiredMixin, StaffuserRequiredMixin, UpdateView):
    login_url = reverse_lazy('entrar')
    group_required = gAdm
    model = Produto
    template_name = 'paginas/form-upload.html'
    fields = ['tipoProduto', 'nome', 'preco', 'descricao', 'vendendo', 'imagem']
    success_url = reverse_lazy('listar-produto')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = 'Atualizar Produto'
        context['botao_submit'] = 'Atualizar'

        return context




class TipoProdutoDelete(GroupRequiredMixin, StaffuserRequiredMixin, DeleteView):
    login_url = reverse_lazy('entrar')
    group_required = gAdm
    model = TipoProduto
    template_name = 'paginas/form-excluir.html'
    success_url = reverse_lazy('listar-tProduto')

class ProdutoDelete(GroupRequiredMixin, StaffuserRequiredMixin, DeleteView):
    login_url = reverse_lazy('entrar')
    group_required = gAdm
    model = Produto
    template_name = 'paginas/form-excluir.html'
    success_url = reverse_lazy('listar-produto')