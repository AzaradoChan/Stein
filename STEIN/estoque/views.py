from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
import datetime
from braces.views import GroupRequiredMixin, StaffuserRequiredMixin

gAdm = [u'Gerência']
gCAdministrativo = [u'Administração'] + gAdm

from .models import TipoProduto, Produto
from mesas.models import Comanda_Produto

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

        data30Dias = datetime.timedelta(days=30)
        dataHoje = datetime.datetime.today()
        prodPedidos = Comanda_Produto.objects.filter(horaPedido__gt=dataHoje-data30Dias)
        produtos = Produto.objects.filter(vendendo=True)

        controle = []
        listaQTDProdutos = []
        for pedido in prodPedidos:
            if pedido.produto.id not in controle:
                controle.append(pedido.produto.id)
                p ={
                    'produto': pedido.produto,
                    'quantidade': int(pedido.quantidade)
                }
                listaQTDProdutos.append(p.copy())
                p.clear()
            else:
                for item in listaQTDProdutos:
                    if item['produto'] == pedido.produto:
                        item['quantidade'] += int(pedido.quantidade)
        
        for prod in produtos:
            if prod.id not in controle:
                p = {
                    'produto': prod,
                    'quantidade': 0
                }

                listaQTDProdutos.append(p.copy())
                p.clear()

        cont = {}
        listaProdutos = sorted(listaQTDProdutos, key=lambda x: x['quantidade'], reverse=True)
        if len(listaProdutos) <= 10:
            cont['prodMPedidos'] = listaProdutos
        else:
            cont['prodMPedidos'] = listaProdutos[0:10]

        listaProdutos = sorted(listaQTDProdutos, key=lambda x: x['quantidade'], reverse=False)
        if len(listaProdutos) <= 10:
            cont['prodMenosPedidos'] = listaProdutos
        else:
            cont['prodMenosPedidos'] = listaProdutos[0:10]


        return qSet, tProdutos, cont



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