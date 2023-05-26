from django.db import models

###################################################################################################
# TABELAS PRINCIPAIS
class Categoria(models.Model):
    nome = models.CharField(max_length=50, unique=True, null=False, blank=False)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return self.nome

class Fabricante(models.Model):
    nome = models.CharField(max_length=50, unique=True, null=False, blank=False)
    
    def __str__(self):
        return self.nome
    
class Componente(models.Model):
    nome = models.CharField(max_length=50, null=False, blank=False)
    modelo = models.CharField(max_length=50, null=False, blank=False)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    preco_custo = models.FloatField(null=False, blank=False)
    fk_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fk_fabricante = models.ForeignKey(Fabricante, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome
    
class Modelo(models.Model):
    nome = models.CharField(max_length=50, unique=True, null=False, blank=False)
    descricao = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.nome
    
class Computador(models.Model):
    nome = models.CharField(max_length=50, null=False, blank=False)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    fk_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fk_modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome
    
class Armazem(models.Model):
    nome = models.CharField(max_length=50, null=False, blank=False)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    endereco = models.CharField(max_length=200, null=False, blank=False)
    volume = models.FloatField(null=False, blank=False, default=10)

    def __str__(self):
        return self.nome
    
class Itens(models.Model):
    quantidade = models.IntegerField(null=False, blank=False, default=1)
    preco_venda = models.FloatField(null=False, blank=False)
    fk_computador = models.ForeignKey(Computador, on_delete=models.CASCADE)

    def __str__(self):
        return self.fk_computador

class Venda(models.Model):
    preco_total = models.FloatField(null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.preco_total
    
###################################################################################################
# TABELAS DE LIGAÇÃO
class Computador_Componente(models.Model):
    fk_computador = models.ForeignKey(Computador, on_delete=models.CASCADE)
    fk_componente = models.ForeignKey(Componente, on_delete=models.CASCADE)

    def __str__(self):
        return self.fk_computador
    
class Armazem_Componente(models.Model):
    quantidade = models.IntegerField(null=False, blank=False, default=1)
    massa = models.FloatField(null=False, blank=False)
    volume = models.FloatField(null=False, blank=False)
    fk_armazem = models.ForeignKey(Armazem, on_delete=models.CASCADE)
    fk_componente = models.ForeignKey(Componente, on_delete=models.CASCADE)

    def __str__(self):
        return self.fk_armazem
    
class Armazem_Computador(models.Model):
    quantidade = models.IntegerField(null=False, blank=False, default=1)
    massa = models.FloatField(null=False, blank=False)
    volume = models.FloatField(null=False, blank=False)
    fk_armazem = models.ForeignKey(Armazem, on_delete=models.CASCADE)
    fk_computador = models.ForeignKey(Computador, on_delete=models.CASCADE)

    def __str__(self):
        return self.fk_armazem
    
class Venda_Itens(models.Model):
    fk_venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    fk_itens = models.ForeignKey(Itens, on_delete=models.CASCADE)

    def __str__(self):
        return self.fk_venda