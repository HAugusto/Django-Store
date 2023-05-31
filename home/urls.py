from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.HomePage, name='home'),
    path('cliente/', views.ClientPageView.ClientPage, name='cliente-page'),
    path('cadastro/', views.RegisterPageView.RegistrationPage, name='cadastro'),
    path('cadastro/armazem/', views.RegisterPageView.StorageRegistrationPage, name='cadastro-armazem'), 
    path('cadastro/componente/', views.RegisterPageView.ComponentRegistrationPage, name='cadastro-componente'),
    path('cadastro/produto/', views.RegisterPageView.ProductRegistrationPage, name='cadastro-produto'),
    path('cadastro/fornecedor/', views.RegisterPageView.SupplierRegistrationPage, name='cadastro-fornecedor'),
    path('cadastro/cliente/', views.RegisterPageView.ClientRegistrationPage, name='cadastro-cliente'),
    path('filial/', views.HomePageView.HomePage, name='filial'),
    path('filial/<slug:id>/', views.HomePageView.HomePage, name='filial-id'),
    path('filial/<slug:id>/inventario/', views.HomePageView.HomePage, name='filial-id-inventario'),
]   