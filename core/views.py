from django.shortcuts import render
from django.views.generic import TemplateView,ListView, CreateView , UpdateView , DeleteView
from .models import TipoProduto,Produto

from .form import ProdutoForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect


from django.shortcuts import render
from django.views import View
from .models import Produto
from django.http import HttpResponseRedirect
from django.urls import reverse


class Index(TemplateView):
    def get(self, request):
        massas = Produto.objects.filter(tipo__nome__icontains='massa')
        esfihas = Produto.objects.filter(tipo__nome__icontains='esfihas')
        pizza = Produto.objects.filter(tipo__nome__icontains='pizza')
        context = {'massas': massas,' esfihas':esfihas, 'pizza':pizza}
        return render(request, 'index.html', context)
    


class Carrinho(ListView):
    template_name = 'carrinho02.html'
    model = Produto
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        
        context['produto'] = Produto.objects.filter()

        return context  
    
def carrinho(request):
    # Obtenha os IDs dos produtos do carrinho armazenados no localStorage
    carrinho_ids = request.GET.getlist('produto', [])

    # Agora, você pode usar esses IDs para buscar os detalhes dos produtos no banco de dados
    # Suponhamos que você tenha um modelo chamado Produto
    produtos_no_carrinho = Produto.objects.filter(id__in=carrinho_ids)

    # Passe os detalhes dos produtos para o template
    context = {'produtos_no_carrinho': produtos_no_carrinho}
    return render(request, 'carrinho0022.html', context)