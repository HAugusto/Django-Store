from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib import messages
from . import forms, models
from .utils.lib_db import getFromDatabase

# Create your views here.
class HomePageView:
    def HomePage(request):        
        
        context = {}
        
        return render(request, template_name='pages/index.html', context=context)

class ClientPageView:
    def ClientPage(request):
        client = getFromDatabase.AboutClient.getAll()
        
        context = {'client_list': client}
        
        return render(request, template_name='pages/read/client.html', context=context)

class RegisterPageView:
    def RegistrationPage(request):
        
        context = {}
        
        return render(request, template_name='pages/register/register.html', context=context)
    
    def StorageRegistrationPage(request):
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
    
    def CategoryRegistrationPage(request):
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
    
    def ComponentRegistrationPage(request):
        category_list = getFromDatabase.AboutCategory.getAll()
        supplier_list = getFromDatabase.AboutSupplier.getAll()
        
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
            
        context = {'form': form, 'category_list': category_list, 'supplier_list': supplier_list}
        
        return render(request, template_name='pages/register/component.html', context=context)
    
    def ProductRegistrationPage(request):
        
        context = {}
        
        return render(request, template_name='pages/register/product.html', context=context)
    
    def SupplierRegistrationPage(request):
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
    
    def ClientRegistrationPage(request):
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