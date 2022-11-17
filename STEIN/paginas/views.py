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
        data30Dias = datetime.timedelta(days=30)
        dataHoje = datetime.datetime.today()
        prodPedidos = mModels.Comanda_Produto.objects.filter(horaPedido__gt=dataHoje-data30Dias)
        produtos = eModels.Produto.objects.filter(vendendo=True)

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

        return cont

class Formulario(TemplateView):
    template_name = 'paginas/form.html'

class Agradecimento(TemplateView):
    template_name = 'paginas/modelo.html'