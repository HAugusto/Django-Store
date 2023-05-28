from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib import messages
from . import forms
from .utils.Database import getFromDatabase

# Create your views here.
class HomePageView:
    def HomePage(request):        
        
        context = {}
        
        return render(request, template_name='pages/index.html', context=context)
    
class RegisterPageView:
    def RegistrationPage(request):
        
        context = {}
        
        return render(request, template_name='pages/register/register.html', context=context)
    
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
    
    def ComponenteRegistrationPage(request):
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
            
        context = {'form': form}
        
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
                try:
                    if not getFromDatabase.ifExists.Client(form.cleaned_data['nome']):
                        form.save()
                        messages.success(request, "Fornecedor cadastrado!")
                        return redirect('/glossario/')
                except Exception as exception:
                    print(str(exception))
                    messages.warning(request, "Equipamento já cadastrado!")
                    pass
            else:
                messages.error(request, "O formulário não foi preenchido corretamente")
        else:
            form = forms.newSupplier()
            
        context = {'form': form}
        
        return render(request, template_name='pages/register/client.html', context=context)