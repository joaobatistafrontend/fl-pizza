from django.shortcuts import render
from django.views.generic import TemplateView
from .models import TipoProduto,Produto

class Index(TemplateView):
    def get(self, request):
        massas = Produto.objects.filter(tipo__nome__icontains='massa')
        esfihas = Produto.objects.filter(tipo__nome__icontains='esfihas')
        context = {'massas': massas,'esfihas':esfihas}
        return render(request, 'index.html', context)
    


class Carrinho(TemplateView):
    template_name = 'carrinho.html'