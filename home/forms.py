from django import forms
from . import models
from django.core.validators import RegexValidator

# Forms - Cadastro de Cliente
class newClient(forms.ModelForm):
    class Meta:
        model = models.Cliente
        fields = '__all__'

# Forms - Cadastro de Fornecedor
class newSupplier(forms.ModelForm):
    class Meta:
        model = models.Fabricante
        fields = ['nome', 'cnpj', 'descricao', 'endereco', 'cidade', 'estado', 'email', 'telefone', 'celular']

# Forms - Cadastro de Componente
class newComponent(forms.ModelForm):
    class Meta:
        model = models.Componente
        fields = '__all__'     

# Forms - Cadastro de Computador
class newComputer(forms.ModelForm):
    class Meta:
        model = models.Computador
        fields = '__all__'

# Forms - Cadastro de Armazém
class newStorage(forms.ModelForm):
    class Meta:
        model = models.Armazem
        fields = '__all__'