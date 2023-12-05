
from django.db import models

class TipoProduto(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    
class TipoValor(models.Model):
    valor_novo = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"R$ {self.valor_novo}"


class Pizzas(models.Model):
    valor = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"R$ {self.valor}"

class ValorMassa(models.Model):
    valor_massa = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"R$ {self.valor_massa}"

class ValorEsfihas(models.Model):
    valor_esfihas = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    def __str__(self):
        return f"R$ {self.valor_esfihas}"
    
class ValorRefriSucos(models.Model):
    valor_refri_sucos = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"R$ {self.valor_refri_sucos}"

class Produto(models.Model):
    tipo = models.ForeignKey(TipoProduto, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='imagens/',blank=True, null=True)
    nome_produto = models.CharField(max_length=100, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    valorPizza = models.ForeignKey(Pizzas, on_delete=models.CASCADE, blank=True, null=True)
    valorMassa = models.ForeignKey(ValorMassa, on_delete=models.SET_NULL, blank=True, null=True)
    valorEsfihas = models.ForeignKey(ValorEsfihas, on_delete=models.SET_NULL, blank=True, null=True)
    valorRefriSucos = models.ForeignKey(ValorRefriSucos, on_delete=models.SET_NULL, blank=True, null=True)
    valorNovo = models.ForeignKey(TipoValor, on_delete=models.SET_NULL, blank=True, null=True)
    def __str__(self):
        if self.valorPizza:
            return f"R$ {Pizzas.valor}"
        elif self.valorMassa:
            return f"R$ {ValorMassa.valor_massa}"
        elif self.valorEsfihas:
            return f"R$ {ValorEsfihas.valor_esfihas})"
        elif self.valorRefriSucos:
            return f"R$ {ValorRefriSucos.valor_refri_sucos}"
        elif self.valorNovo:
            return f"R$ {TipoValor.valor_novo}"
        return f"{self.tipo}: {self.nome_produto}"
    




    