from django.urls import path
from . import views

urlpatterns = [
    path('', views.ReadPageView.HomePage, name='home'),
    
    path('armazens/', views.ReadPageView.SupplierPage, name='tabela-armazem'),
    path('filiais/', views.ReadPageView.ClientPage, name='tabela-filial'),
    path('clientes/', views.ReadPageView.ClientPage, name='tabela-cliente'),
    path('fornecedores/', views.ReadPageView.SupplierPage, name='tabela-fornecedor'),
    path('componentes/', views.ReadPageView.ComponentPage, name='tabela-componente'),
    path('componente/<int:id>/', views.UpdatePageView.ComponentIDPage, name='tabela-componente-id'),
    path('produtos/', views.ReadPageView.ClientPage, name='tabela-produto'),

    path('cadastro/', views.CreatePageView.RegistrationPage, name='cadastro'),
    path('armazem/cadastrar/', views.CreatePageView.StoragePage, name='cadastro-armazem'), 
    path('componente/cadastrar/', views.CreatePageView.ComponentPage, name='cadastro-componente'),
    path('produto/cadastrar/', views.CreatePageView.ProductPage, name='cadastro-produto'),
    path('fornecedor/cadastrar/', views.CreatePageView.SupplierPage, name='cadastro-fornecedor'),
    path('cliente/cadastrar/', views.CreatePageView.ClientPage, name='cadastro-cliente'),
    
    path('filial/', views.ReadPageView.HomePage, name='filial'),
    path('filial/<slug:id>/', views.ReadPageView.HomePage, name='filial-id'),
    path('filial/<slug:id>/inventario/', views.ReadPageView.HomePage, name='filial-id-inventario'),
    
    path('armazem/<int:id>/', views.UpdatePageView.StoragePage, name='editar-armazem'), 
    path('componente/<int:id>/', views.UpdatePageView.ComponentIDPage, name='editar-componente'),
    path('produto/<int:id>/', views.UpdatePageView.ProductPage, name='editar-produto'),
    path('fornecedor/<int:id>/', views.UpdatePageView.SupplierIDPage, name='editar-fornecedor'),
    path('cliente/<int:id>/', views.UpdatePageView.ClientPage, name='editar-cliente'),

    path('filial/<int:id>/remover/', views.DeletePageView, name='remover-filial'),
    path('cliente/<int:id>/remover/', views.DeletePageView.ClientPage, name='remover-cliente'),
    path('fornecedor/<int:id>/remover/', views.DeletePageView.SupplierPage, name='remover-fornecedor'),
    path('componente/<int:id>/remover/', views.DeletePageView.ClientPage, name='remover-componente'),
    path('produtos/<int:id>/remover/', views.DeletePageView.ClientPage, name='remover-produto'),
]   