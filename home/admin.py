from django.contrib import admin
from home import models

# Register your models here.

admin.site.register(models.Categoria)
admin.site.register(models.Fabricante)
admin.site.register(models.Cliente)

admin.site.register(models.Computador)
admin.site.register(models.Armazem)
admin.site.register(models.Itens)
admin.site.register(models.Venda)

admin.site.register(models.Computador_Componente)
admin.site.register(models.Armazem_Componente)
admin.site.register(models.Armazem_Computador)
admin.site.register(models.Venda_Itens)
