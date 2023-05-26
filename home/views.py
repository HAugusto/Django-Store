from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView:
    def HomePage(request):        
        
        context = {}
        
        return render(request, template_name='pages/index.html', context=context)
    
class RegisterPageView:
    def RegistrationPage(request):
        
        context = {}
        
        return render(request, template_name='pages/register/register.html', context=context)
        
    def ProductRegistrationPage(request):
        
        context = {}
        
        return render(request, template_name='pages/register/product.html', context=context)
    
    def SupplierRegistrationPage(request):
        
        context = {}
        
        return render(request, template_name='pages/register/supplier.html', context=context)
    
    def ClientRegistrationPage(request):
        
        context = {}
        
        return render(request, template_name='pages/register/client.html', context=context)