from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(TipoProduto)
class TipoProdADM(admin.ModelAdmin):
     list_display = ('nome',)

@admin.register(TipoValor)
class TipoProdADM(admin.ModelAdmin):
     list_display = ('valor_novo',)

@admin.register(Produto)
class ProdutoADM(admin.ModelAdmin):
     list_display = ('tipo', 'nome_produto', 'descricao', 'valorPizza', 'valorMassa', 'valorEsfihas', 'valorRefriSucos',)

@admin.register(Pizzas)
class TamanhoPizzaADM(admin.ModelAdmin):
     list_display = ('valor',)

@admin.register(ValorMassa)
class TamanhoMassa(admin.ModelAdmin):
     list_display = ('valor_massa',)


@admin.register(ValorEsfihas)
class EsfihasADM(admin.ModelAdmin):
     list_display = ('valor_esfihas',)

@admin.register(ValorRefriSucos)
class TamanhoMassa(admin.ModelAdmin):
     list_display = ('valor_refri_sucos',)
