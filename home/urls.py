from django.urls import path
from . import views

urlpatterns = [
    path('', views.ReadPageView.HomePage, name='home'),
    
    # READ - FUNCIONANDO
    path('armazens/', views.ReadPageView.StoragePage, name='tabela-armazem'),
    path('filiais/', views.ReadPageView.ClientPage, name='tabela-filial'),
    path('clientes/', views.ReadPageView.ClientPage, name='tabela-cliente'),
    path('fornecedores/', views.ReadPageView.SupplierPage, name='tabela-fornecedor'),
    path('componentes/', views.ReadPageView.ComponentPage, name='tabela-componente'),
    path('componente/<int:id>/', views.UpdatePageView.ComponentIDPage, name='tabela-componente-id'),
    path('produtos/', views.ReadPageView.ClientPage, name='tabela-produto'),

    # CREATE - FUNCIONANDO
    path('cadastro/', views.CreatePageView.RegistrationPage, name='cadastro'),
    path('armazem/cadastrar/', views.CreatePageView.StoragePage, name='cadastro-armazem'), 
    path('componente/cadastrar/', views.CreatePageView.ComponentPage, name='cadastro-componente'),
    path('produto/cadastrar/', views.CreatePageView.ProductPage, name='cadastro-produto'),
    path('fornecedor/cadastrar/', views.CreatePageView.SupplierPage, name='cadastro-fornecedor'),
    path('cliente/cadastrar/', views.CreatePageView.ClientPage, name='cadastro-cliente'),
    
    path('filial/', views.ReadPageView.HomePage, name='filial'),
    path('filial/<int:id>/', views.ReadPageView.HomePage, name='filial-id'),
    path('filial/<int:id>/inventario/', views.ReadPageView.HomePage, name='filial-id-inventario'),
    
    # UPDATE - FUNCIONANDO 
    path('armazem/<int:id>/', views.UpdatePageView.StorageIDPage, name='editar-armazem'), 
    path('componente/<int:id>/', views.UpdatePageView.ComponentIDPage, name='editar-componente'),
    path('produto/<int:id>/', views.UpdatePageView.ProductPage, name='editar-produto'), # REVISAR
    path('fornecedor/<int:id>/', views.UpdatePageView.SupplierIDPage, name='editar-fornecedor'),
    path('cliente/<int:id>/', views.UpdatePageView.ClientPage, name='editar-cliente'),

    # DELETE - FUNCIONANDO
    path('armazem/<int:id>/remover/', views.DeletePageView, name='remover-armazem'),
    path('cliente/<int:id>/remover/', views.DeletePageView.ClientPage, name='remover-cliente'),
    path('fornecedor/<int:id>/remover/', views.DeletePageView.SupplierPage, name='remover-fornecedor'),
    path('componente/<int:id>/remover/', views.DeletePageView.ComponentPage, name='remover-componente'),
    path('produtos/<int:id>/remover/', views.DeletePageView.ProductPage, name='remover-produto'),
]   