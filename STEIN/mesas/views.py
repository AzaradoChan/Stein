import json
import django.http as http
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


from braces.views import GroupRequiredMixin, StaffuserRequiredMixin

from equipe.models import Funcionario
from estoque.models import Produto, TipoProduto
from moduloEmail.models import EmailAnonimo

from .models import Mesa, Comanda, Comanda_Produto

gViewCom = [u'Retaguarda']
gruposComanda = [u'Linha de Frente']
gAdm = [u'Gerência']
gCAdministrativo = [u'Administração'] + gAdm

# Create your views here.
class ComandaCreate(ListView):
    model = Produto
    template_name = 'paginas/form-comanda.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = 'Fazer Pedido'
        context['botao_submit'] = 'Próximo'
        context['modelo'] = 'create'
        context['telefone'] = 'S'


        return context
    
    def get_queryset(self):
        busca = Produto.objects.exclude(vendendo=False).order_by('tipoProduto_id')
        tiposProduto = TipoProduto.objects.all().order_by('tipo')
        if (self.request.user.is_anonymous):
            funcionarios = Funcionario.objects.filter(cpf='000.000.000-00')
        else:
            funcionarios = Funcionario.objects.filter(demitido=False)
        mesas = Mesa.objects.all()

        return busca, tiposProduto, funcionarios, mesas

def criarComanda(request):
    if request.method == 'GET':
        try:
            mesaPK = request.GET['mesaPK']
            funcPK = request.GET['funcPK']
            prodPK = json.loads(request.GET['produtoPK'])
            prodQTD = json.loads(request.GET['produtoQTD'])
            observacao = request.GET['observacao']
            mod = request.GET['modelo']
                
            m = Mesa.objects.filter(pk=mesaPK, ocupada=True)
            c = Comanda.objects.filter(nmrMesa_id=mesaPK, encerrada=False)
            if len(m) == 1 and len(c) == 1 and mod =='update':
                if len(prodPK) > 0:
                    for p in prodPK:
                        try:
                            cProd = Comanda_Produto.objects.get(produto_id=p, comanda_id=c[0].id)
                        except Comanda_Produto.DoesNotExist:
                            Comanda_Produto.objects.create(
                                comanda_id=c[0].id,
                                produto_id=p,
                                quantidade= prodQTD[prodPK.index(p)]
                            )
                        else:
                            if prodQTD[prodPK.index(p)] == '0':
                                cProd.delete()
                            else:
                                # cProd.quantidade = prodQTD[prodPK.index(p)]
                                if int(prodQTD[prodPK.index(p)]) < int(cProd.quantidadeEntregue):
                                    cProd.quantidade = prodQTD[prodPK.index(p)]
                                    cProd.quantidadeEntregue = prodQTD[prodPK.index(p)]
                                else:
                                    cProd.quantidade = prodQTD[prodPK.index(p)]
                                cProd.save()


                AtualizaValTotComanda(c[0])
                return http.HttpResponseRedirect(reverse_lazy('listar-comanda'))
                
            elif len(m) >= 1 or len(c) >= 1 and mod == 'create':
                return http.HttpResponseRedirect(reverse_lazy('cad-comanda'), 'A mesa escolhida já está cheia.')

            elif len(m) < 1 and len(c) < 1 and mod=='create':
                com = 0
                try:
                    email = request.GET['email']
                except:
                    com = Comanda(nmrMesa_id=mesaPK, funcionario_id=funcPK)
                else:
                    cAnon = EmailAnonimo.objects.get(email=email)
                    com = Comanda(nmrMesa_id=mesaPK, funcionario_id=funcPK, contaAnon=cAnon)
                com.save()
                for prod in prodPK:
                    if prodQTD[prodPK.index(prod)] != 0:
                        cProd = Comanda_Produto.objects.create(comanda_id=com.id, 
                        produto_id=prod, 
                        quantidade=prodQTD[prodPK.index(prod)])
                        cProd.save()
                com.observacao = observacao
                AtualizaValTotComanda(com)
                com.save()
                
                mesa = Mesa.objects.get(id=mesaPK)
                mesa.ocupada = True
                mesa.save()
                return http.HttpResponseRedirect(reverse_lazy('listar-comanda'))
        except Exception as e:
            return http.HttpResponseBadRequest()
    else:
        return http.HttpResponseForbidden()

def visualizarAutoPedido(request):
    if request.method == 'GET':
        return http.HttpResponse('Tudo Ok', 200)
    else:
        return http.HttpResponseForbidden()

class ComandaList(GroupRequiredMixin, ListView):
    login_url = reverse_lazy('entrar')
    group_required = gruposComanda + gCAdministrativo + gViewCom
    model = Comanda
    template_name = 'paginas/listas/comandas.html'

    def get_queryset(self): 
        aberta = self.request.GET.get('encerrado')
        data = self.request.GET.get('dataAbertura')
        comandas = 0
        listaPedidos = 0 
        if aberta == 'True' and data == '':
            comandas = Comanda.objects.filter(encerrada=False)
            listaPedidos = Comanda_Produto.objects.all().exclude(comanda__encerrada=False).values()
        elif aberta == 'False' and data == '':
            comandas = Comanda.objects.filter(encerrada=True)
            listaPedidos = Comanda_Produto.objects.all().exclude(comanda__encerrada=True).values()
        elif aberta == 'none' and data != '':
            comandas = Comanda.objects.filter(dataCriada=str(data))
            listaPedidos = Comanda_Produto.objects.all().exclude(comanda__dataCriada=str(data)).values()
        elif aberta == 'True' and data != '':
            comandas = Comanda.objects.filter(encerrada=False, dataCriada=str(data))
            listaPedidos = Comanda_Produto.objects.all().exclude(comanda__encerrada=False, comanda__dataCriada=str(data)).values()
        elif aberta == 'False' and data != '':
            comandas = Comanda.objects.filter(encerrada=True, dataCriada=str(data))
            listaPedidos = Comanda_Produto.objects.all().exclude(comanda__encerrada=True, comanda__dataCriada=str(data)).values()
        else: 
            comandas = Comanda.objects.filter(encerrada=False)
            listaPedidos = Comanda_Produto.objects.all().values()

        return comandas, listaPedidos

class VerComandaAnonList(ListView):
    template_name = 'paginas/viewPedidoAnon.html'
    model = Comanda
    
    def get_context_data(self, *args, **kwargs):
        cont = super().get_context_data(*args, **kwargs)

        cont['titulo'] = f'Produtos Pedidos'
        cont['botao_submit'] = 'Atualizar'
        cont['modelo'] = 'update'
        
        return cont

    def get_queryset(self, *args, **kwargs):
        query = Comanda.objects.get(contaAnon__pk=self.kwargs['codigo_anon'], encerrada=False)
        produtos = Comanda_Produto.objects.filter(comanda=query)
        return query, produtos

class ComandaDelete(GroupRequiredMixin, StaffuserRequiredMixin, DeleteView):
    login_url = reverse_lazy('entrar')
    group_required = gCAdministrativo
    model = Comanda
    template_name = 'paginas/form-excluir.html'
    success_url = reverse_lazy('listar-comanda')

    def post(self, request, *args, **kwargs):
        
        if self.get_object().encerrada == False:
            mesa = Mesa.objects.get(id=self.get_object().nmrMesa_id)
            mesa.ocupada = False
            mesa.save()
        
        resp = super().post(request, *args, **kwargs)


        return resp


class ComandaProdutoList(GroupRequiredMixin, UpdateView):
    login_url = reverse_lazy('entrar')
    group_required = gruposComanda + gCAdministrativo + gViewCom
    model = Comanda_Produto
    template_name = 'paginas/form-prodCom.html'
    fields = ['produto', 'quantidade']
    success_url = reverse_lazy('listar-comanda')

    def get_context_data(self, **kwargs):
        cont = super().get_context_data(**kwargs)
        cont['modelo'] = 'update'
        return cont


    def get_queryset(self, *args, **kwargs):
        prodComanda = Comanda_Produto.objects.filter(comanda_id=kwargs.get('comanda_id'))
        return prodComanda


class ComandaRetaguardaList(GroupRequiredMixin, ListView):
    login_url  = reverse_lazy('entrar')
    group_required = gAdm + gViewCom
    model = Comanda
    template_name = 'paginas/comandas-retaguarda.html'

    def get_context_data(self, **kwargs):
        cont = super().get_context_data(**kwargs)

        cont['titulo'] = 'Pratos não entregues.'

        return cont
    
    def get_queryset(self):
        comandas = Comanda.objects.filter(encerrada=False).order_by('dataHoraCriada')
        prodCom = []
        for com in comandas:
            c = {'produtos': []}
            c['comanda'] = com
            produtos = Comanda_Produto.objects.filter(comanda_id=c['comanda'].id)
            for p in produtos:
                if p.quantidadeEntregue < p.quantidade:
                    c['produtos'].append(p)

            prodCom.append(c)
        return comandas, prodCom

class ComandaProdutoList(GroupRequiredMixin, ListView):
    login_url = reverse_lazy('entrar')
    group_required = gruposComanda + gCAdministrativo + gViewCom
    model = Comanda_Produto
    template_name = 'paginas/form-comanda.html'

    def get_context_data(self, *args, **kwargs):
        cont = super().get_context_data(*args, **kwargs)

        cont['titulo'] = f'Produtos da comanda {self.kwargs["comanda_id"]}'
        cont['botao_submit'] = 'Atualizar'
        cont['modelo'] = 'update'
        return cont

    def get_queryset(self):
        tiposProduto = TipoProduto.objects.all().order_by('tipo')
        busca = Produto.objects.exclude(vendendo=False).order_by('tipoProduto_id')
        com = Comanda.objects.get(id=self.kwargs['comanda_id'])
        funcionario = Funcionario.objects.filter(id=com.funcionario_id)

        prodPedidos = Comanda_Produto.objects.filter(comanda_id=self.kwargs['comanda_id'])
        mesas = Mesa.objects.all()

        return busca, tiposProduto, funcionario, mesas, prodPedidos

def atualizarProdutoComanda(GroupRequiredMixin, request):
    login_url = reverse_lazy('entrar')
    group_required = gruposComanda + gCAdministrativo
    if request.method == 'GET':
        try:
            pedido_id = int(request.GET['pedidoID'])
            produto_id = int(request.GET['produtoID'])
            qtdProduto = int(request.GET['qtdProduto'])
            pedido = Comanda_Produto.objects.get(pk=pedido_id, produto=produto_id)
            pedido.quantidade = qtdProduto
            pedido.save()
            
            comanda = Comanda.objects.get(pk=pedido.comanda.pk)
            AtualizaValTotComanda(comanda)
        except:
            return http.HttpResponseBadRequest()
        else:
            return http.HttpResponse('')
    else:
        return http.HttpResponseForbidden()
        
def atualizarPedido(request):
    if request.method == 'GET':
        comPK = request.GET['comandaPK']
        produtos = json.loads(request.GET['produtosPK'])
        quantidade = json.loads(request.GET['quantidadeProd'])
        for prod in produtos:
            pedido = Comanda_Produto.objects.get(comanda_id=comPK, produto_id=prod)
            qtd = int(quantidade[produtos.index(prod)]) + int(pedido.quantidadeEntregue)
            pedido.quantidadeEntregue = qtd
            pedido.save()
        return http.HttpResponseRedirect(reverse_lazy('listar-retaguarda'))
    else:
        return http.HttpResponseForbidden()

def atualizarValorPagoComanda(request):
    if request.method == 'GET':
        encerrar = request.GET['encerrada']
        print(encerrar)
        valPago = request.GET['valorPago']
        valPago = float(valPago.replace(',', '.'))
        comandaPK = request.GET['comandaPK']
        comanda = Comanda.objects.get(id=comandaPK, encerrada=False)
        if encerrar == 'false':
            comanda.valorPago = valPago
        else:
            comanda.valorPago = comanda.valorTotal
            comanda.encerrada = True
            mesa = Mesa.objects.get(pk=comanda.nmrMesa_id)
            mesa.ocupada = False
            mesa.save()
        comanda.save()

        return http.HttpResponseRedirect(reverse_lazy('listar-comanda'))
    else:
        return http.HttpResponseForbidden()

def AtualizaValTotComanda(comanda, retorna=False):
    cP = Comanda_Produto.objects.filter(comanda_id=comanda.pk)
    com_prod = cP.values_list()
    val_prod = []
    qtd_prod = []
    for prod in com_prod:
        val_prod.append(Produto.objects.filter(pk=prod[2]).values()[0]['preco'])
        if float(prod[3]) == 0:
            Comanda_Produto.objects.get(id=prod[0]).delete()
        qtd_prod.append(prod[3])
    valor = 0
    for val in val_prod:
        valor += float(val) * qtd_prod[val_prod.index(val)]
    if retorna:
        return valor
    else:
        comanda.valorTotal = valor
        comanda.save()
