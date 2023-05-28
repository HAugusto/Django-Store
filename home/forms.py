from django import forms
from . import models
from django.core.validators import RegexValidator

# Forms - Cadastro de Cliente
class newClient(forms.ModelForm):
    class Meta:
        model = models.Cliente
        fields = '__all__'

# Forms - Cadastro de Fornecedor - Implementado
class newSupplier(forms.ModelForm):
    class Meta:
        model = models.Fabricante
        fields = '__all__'

# Forms - Cadastro de Categoria - Implementado
class newCategory(forms.ModelForm):
    class Meta:
        model = models.Categoria
        fields = '__all__'
    
# Forms - Cadastro de Componente - Implementado
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