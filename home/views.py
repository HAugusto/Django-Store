from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.contrib import messages
from . import forms, models
from .utils.lib_db import getFromDatabase

class CreatePageView:
    def RegistrationPage(request):
        
        context = {}
        
        return render(request, template_name='pages/register/register.html', context=context)
    
    def StoragePage(request):
        if request.method == 'POST':
            form = forms.newStorage(request.POST)
            
            if form.is_valid():
                form.save()
                messages.success(request, "Armazem cadastrado!")
                return redirect('/')
            else:
                messages.error(request, "O formulário não foi preenchido corretamente")
        else:
            form = forms.newStorage()
        
        context = {'form': form}
        
        return render(request, template_name='pages/register/storage.html', context=context) 
    
    def CategoryPage(request):
        if request.method == 'POST':
            form = forms.newCategory(request.POST)
            
            if form.is_valid():
                form.save()
                messages.success(request, "Nova categoria cadastrada!")
                return redirect('/')
            else:
                messages.error(request, "O formulário não foi preenchido corretamente")
        else:
            form = forms.newCategory()
            
        context = {'form': form}
        
        return render(request, template_name='pages/register/category.html', context=context)
    
    def ComponentPage(request):
        category_list = getFromDatabase.AboutCategory.getAll()
        supplier_list = getFromDatabase.AboutSupplier.getAll()
        model_list = models.Modelo.objects.all()
        
        if request.method == 'POST':
            form = forms.newComponent(request.POST)
            
            if form.is_valid():
                form.save()
                messages.success(request, "Novo componente cadastrado!")
                return redirect('/')
            else:
                messages.error(request, "O formulário não foi preenchido corretamente")
        else:
            form = forms.newComponent()
            
        context = {'form': form, 'category_list': category_list, 'supplier_list': supplier_list, 'model_list': model_list}

        
        return render(request, template_name='pages/register/component.html', context=context)
    
    def ProductPage(request):
        model_list = models.Modelo.objects.filter(is_component = False)
        category_list = models.Categoria.objects.filter(is_component = False)
        
        motherboard_list = models.Componente.objects.filter(fk_categoria__nome = 'Placa-Mãe')
        processor_list = models.Componente.objects.filter(fk_categoria__nome = 'Processador')
        ram_memory_list = models.Componente.objects.filter(fk_categoria__nome = 'Memória RAM')
        video_card_list = models.Componente.objects.filter(fk_categoria__nome = 'Placa de Vídeo')
        power_supply_list = models.Componente.objects.filter(fk_categoria__nome = 'Fonte')
        cabinet_list = models.Componente.objects.filter(fk_categoria__nome = 'Gabinete')
        
        if request.method == 'POST':
            form = forms.newComputer(request.POST)
            
            if form.is_valid():
                fk_computador = form.save()
                
                forms.newComputerComponent(request.POST)
            
                messages.success(request, "Produto cadastrado!")
                return redirect('/')    
            else:
                messages.error(request, "O formulário não foi preenchido corretamente")
        else:
            form = forms.newComputer()
            
        context = {'model_list': model_list, 'category_list': category_list, 'motherboard_list': motherboard_list, 'processor_list': processor_list, 'ram_memory_list': ram_memory_list, 'video_card_list': video_card_list, 'power_supply_list': power_supply_list, 'cabinet_list': cabinet_list, 'form': form}
        
        return render(request, template_name='pages/register/product.html', context=context)
    
    def SupplierPage(request):
        if request.method == 'POST':
            form = forms.newSupplier(request.POST)
            
            if form.is_valid():
                form.save()
                messages.success(request, "Fornecedor cadastrado!")
                return redirect('/')
            else:
                messages.error(request, "O formulário não foi preenchido corretamente")
        else:
            form = forms.newSupplier()
        
        context = {'form': form}
        
        return render(request, template_name='pages/register/supplier.html', context=context)
    
    def ClientPage(request):
        if request.method == 'POST':
            form = forms.newClient(request.POST)
            
            if form.is_valid():
                form.save()
                messages.success(request, "Fornecedor cadastrado!")
                return redirect('/')
            else:
                messages.error(request, "O formulário não foi preenchido corretamente")
        else:
            form = forms.newSupplier()
            
        context = {'form': form}
        
        return render(request, template_name='pages/register/client.html', context=context)
    
class ReadPageView:
    def HomePage(request):        
        
        context = {}
        
        return render(request, template_name='pages/index.html', context=context)
    
    def StoragePage(request):
        storage_list = getFromDatabase.AboutStorage.getAll()
        
        context = {'storage_list': storage_list}
        
        return render(request, template_name='pages/read/storage.html', context=context)

    def SupplierPage(request):
        supplier_list = getFromDatabase.AboutSupplier.getAll()
        
        context = {'supplier_list': supplier_list}
        
        return render(request, template_name='pages/read/supplier.html', context=context)
    
    def ClientPage(request):
        client = getFromDatabase.AboutClient.getAll()
        
        context = {'client_list': client}
        
        return render(request, template_name='pages/read/client.html', context=context)
    
    def ComponentPage(request):
        component_list = getFromDatabase.AboutComponent.getAll()
        
        context = {'component_list': component_list}
        
        return render(request, template_name='pages/read/component.html', context=context)

class UpdatePageView:
    def StorageIDPage(request, id):
        try:
            storage = models.Armazem.objects.get(id=id)
        except models.Armazem.DoesNotExist:
            storage = None

        if request.method == 'POST':
            form = forms.updateStorage(request.POST, instance=storage)
            
            if form.is_valid():
                storage = form.save()                
                messages.success(request, "Item atualizado com sucesso!")
                return redirect('/fornecedores/')
            else:
                messages.error(request, "O formulário não foi preenchido corretamente")
        else:
            form = forms.updateStorage(instance=storage)
        
        context = {'storage': storage, 'form': form}
        
        return render(request, template_name='pages/update/storageid.html', context=context)
             
    def SupplierIDPage(request, id):
        try:
            supplier = models.Fabricante.objects.get(id=id)
        except models.Fabricante.DoesNotExist:
            supplier = None

        if request.method == 'POST':
            form = forms.updateSupplier(request.POST, instance=supplier)
            
            if form.is_valid():
                supplier = form.save()                
                messages.success(request, "Item atualizado com sucesso!")
                return redirect('/fornecedores/')
            else:
                messages.error(request, "O formulário não foi preenchido corretamente")
        else:
            form = forms.updateSupplier(instance=supplier)
        
        context = {'supplier': supplier, 'form': form}
        
        return render(request, template_name='pages/update/supplierid.html', context=context)
    
            
    def ClientPage(request, id):
        try:
            client = models.Cliente.objects.get(id=id)
        except models.Cliente.DoesNotExist:
            client = None

        if request.method == 'POST':
            form = forms.updateClient(request.POST, instance=client)
            
            if form.is_valid():
                client = form.save()                
                messages.success(request, "Item atualizado com sucesso!")
                return redirect('/fornecedores/')
            else:
                messages.error(request, "O formulário não foi preenchido corretamente")
        else:
            form = forms.updateClient(instance=client)
        
        context = {'client': client, 'form': form}
        
        return render(request, template_name='pages/update/clientid.html', context=context)
        
    def ComponentIDPage(request, id):
        try:
            component = models.Componente.objects.get(id=id)
        except models.Componente.DoesNotExist:
            component = None

        if request.method == 'POST':
            form = forms.updateComponent(request.POST, instance=component)
            
            if form.is_valid():
                component = form.save()                
                messages.success(request, "Item atualizado com sucesso!")
                return redirect('/componentes/')
            else:
                messages.error(request, "O formulário não foi preenchido corretamente")
        else:
            form = forms.updateComponent(instance=component)
        
        context = {'component': component, 'form': form}
        
        return render(request, template_name='pages/update/componentid.html', context=context)
    
    def ProductPage(request, id):
        tag = get_object_or_404(models.Computador, id=id)

        if request.method == 'POST':
            tag.delete()
            return redirect('/glossario/')
    
class DeletePageView:
    def SupplierPage(request, id):
        tag = get_object_or_404(models.Fabricante, id=id)

        if request.method == 'POST':
            tag.delete()
            return redirect('/fornecedores/')
        
    def ClientPage(request, id):
        tag = get_object_or_404(models.Cliente, id=id)

        if request.method == 'POST':
            tag.delete()
            return redirect('/clientes/')
        
    def ComponentPage(request, id):
        tag = get_object_or_404(models.Componente, id=id)

        if request.method == 'POST':
            tag.delete()
            return redirect('/componentes/')
        
    def ProductPage(request, id):
        tag = get_object_or_404(models.Computador, id=id)

        if request.method == 'POST':
            tag.delete()
            return redirect('/produtos/')