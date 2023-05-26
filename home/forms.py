from django import forms
from . import models
from django.core.validators import RegexValidator

class novaFabricante(forms.ModelForm):
    class Meta:
        model = models.Fabricante
        fields = '__all__'

class newComponent(forms.ModelForm):
    class Meta:
        model = models.Componente
        fields = '__all__'     
        
class newStorage(forms.ModelForm):
    class Meta:
        model = models.Armazem
        fields = '__all__'

class newTag(forms.ModelForm):
    # Formatação: XYZ123_ABC
    glossario = forms.CharField(required=True)
    numero = forms.IntegerField(min_value=0, max_value=9999, required=True)
    fk_tag_glossario = forms.IntegerField(required=True)
        
    def __init__(self, *args, **kwargs):
        self.fk_tag_glossario = kwargs.pop('fkg', None)
        super().__init__(*args, **kwargs)

    def clean(self):
        data = super().clean()
        glossario = data.get('glossario')
        numero = data.get('numero')
        fk_tag_glossario = self.fk_tag_glossario

        tag = f"{glossario.replace('*', '')}{numero}"
        
        del(data['glossario'])
        del(data['numero'])

        data['tag'] = tag

        print(data)

        return data
    
    class Meta:
        model = models.Tags
        fields = ['tag', 'fk_tag_glossario', 'fk_planta']