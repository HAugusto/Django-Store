from django.core.exceptions import ValidationError
from django.db import models

###################################################################################################
# TABELAS ABSTRATAS   
class EnderecoMixin(models.Model):
    endereco = models.CharField(max_length=200, null=False, blank=False)
    cidade = models.CharField(max_length=100, null=False, blank=False)
    estado = models.CharField(max_length=150, null=False, blank=False)
    
    class Meta:
        abstract = True
        
class ContatoMixin(models.Model):
    email = models.CharField(max_length=50, unique=True, null=True, blank=True)
    telefone = models.CharField(max_length=14, unique=True, null=True, blank=True)
    celular = models.CharField(max_length=20, unique=True, null=True, blank=True)
    
    class Meta:
        abstract = True
    
class TimestampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
     
    class Meta:
        abstract = True
           
# TABELAS PRINCIPAIS
class Categoria(TimestampMixin):
    nome = models.CharField(max_length=50, unique=True, null=False, blank=False)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return self.nome

class Cliente(EnderecoMixin, ContatoMixin, TimestampMixin):
    nome = models.CharField(max_length=100, null=False, blank=False)
    is_pessoa_fisica = models.BooleanField(default=True)
    cpf = models.CharField(max_length=14, unique=True, blank=True, null=True)
            
    def __str__(self):
        return self.nome    
    
class Fabricante(EnderecoMixin, ContatoMixin, TimestampMixin):
    nome = models.CharField(max_length=50, null=False, blank=False)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    cnpj = models.CharField(max_length=18, unique=True, null=False, blank=False)
    
    def __str__(self):
        return self.nome
    
class Modelo(TimestampMixin):
    nome = models.CharField(max_length=50, unique=True, null=False, blank=False)
    descricao = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.nome

class Componente(TimestampMixin):
    nome = models.CharField(max_length=50, null=False, blank=False)
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    preco_custo = models.FloatField(null=False, blank=False)
    fk_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fk_fabricante = models.ForeignKey(Fabricante, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome
    
class Computador(TimestampMixin):
    nome = models.CharField(max_length=50, null=False, blank=False)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    fk_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fk_modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome
    
class Armazem(TimestampMixin, EnderecoMixin):
    nome = models.CharField(max_length=50, null=False, blank=False)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    volume = models.FloatField(null=False, blank=False, default=10)

    def __str__(self):
        return self.nome
    
class Itens(TimestampMixin):
    preco_venda = models.FloatField(null=False, blank=False)
    fk_computador = models.ForeignKey(Computador, on_delete=models.CASCADE)

    def __str__(self):
        return self.fk_computador

class Venda(TimestampMixin):
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
    quantidade = models.IntegerField(null=False, blank=False, default=1)
    preco_item = models.FloatField(null=False, blank=False)

    def __str__(self):
        return self.fk_venda