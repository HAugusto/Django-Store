from home import models 
from django.db import transaction
import pandas

class Import():
    @staticmethod
    # Importa os dados de equipamento de um arquivo excel
    def importarFornecedor (excel_file):
        sheet_name = 'home_fornecedor'
        to_register = []
        
        __file__ = pandas.read_excel(excel_file, sheet_name)

        for _, row in __file__.iterrows():
            endereco = row['endereco']
            cidade = row['cidade']
            estado = row['estado']
            email = row['email']
            telefone = row['telefone']
            celular = row['celular']
            nome = row['nome']
            descricao = row['descricao']
            cnpj = row['cnpj']
                
            try:
                fabricante = models.Fabricante.objects.get(nome = nome)
            except models.Fabricante.DoesNotExist:
                fabricante = models.Fabricante(nome = nome, descricao = descricao, endereco = endereco, cidade = cidade, estado = estado, email = email, telefone = telefone, celular = celular, cnpj = cnpj)
                
                if Verify.check_list(to_register, fabricante, 'nome'):
                    to_register.append(fabricante)
            
        Register.register(to_register, models.Fabricante, 'nome')
        return True
        
    def importarCategorias (excel_file):
        sheet_name = 'home_categoria'
        to_register = []
        
        __file__ = pandas.read_excel(excel_file, sheet_name)

        for _, row in __file__.iterrows():
            nome = row['nome']
            descricao = row['descricao']
            is_component = row['is_component']
                
            try:
                categoria = models.Categoria.objects.get(nome = nome)
            except models.Categoria.DoesNotExist:
                categoria = models.Categoria(nome = nome, descricao = descricao, is_component = is_component)
                
                if Verify.check_list(to_register, categoria, 'nome'):
                    to_register.append(categoria)
            
        Register.register(to_register, models.Categoria, 'nome')
        return True
    
    def importarModelos (excel_file):
        sheet_name = 'home_modelo'
        to_register = []
        
        __file__ = pandas.read_excel(excel_file, sheet_name)

        for _, row in __file__.iterrows():
            nome = row['nome']
            descricao = row['descricao']
            is_component = row['is_component']
                
            try:
                modelo = models.Modelo.objects.get(nome = nome)
            except models.Modelo.DoesNotExist:
                modelo = models.Modelo(nome = nome, descricao = descricao, is_component = is_component)
                
                if Verify.check_list(to_register, modelo, 'nome'):
                    to_register.append(modelo)
            
        Register.register(to_register, models.Modelo, 'nome')
        return True
    
    def importarComponentes (excel_file):
        sheet_name = 'home_componente'
        to_register = []
        
        __file__ = pandas.read_excel(excel_file, sheet_name)

        for _, row in __file__.iterrows():
            nome = row['nome']
            descricao = row['descricao']
            preco_custo = row['preco_custo']
            fk_categoria = row['fk_categoria_id']
            fk_fabricante = row['fk_fabricante_id']
            fk_modelo = row['modelo_id']

            try:
                fabricante = models.Componente.objects.get(nome = nome)
            except models.Componente.DoesNotExist:
                categoria = models.Categoria.objects.get(nome = fk_categoria)
                fabricante = models.Fabricante.objects.get(nome = fk_fabricante)
                modelo = models.Modelo.objects.get(nome = fk_modelo)
                componente = models.Componente(nome = nome, descricao = descricao, preco_custo = preco_custo, fk_categoria = categoria, fk_fabricante = fabricante, modelo = modelo)
                
                if Verify.check_list(to_register, componente, 'nome'):
                    to_register.append(componente)
            
        Register.register(to_register, models.Componente, 'nome')
        return True
    
class Verify:
    def check_list(to_register, object, attribute):
        if to_register:
                        
            for temp in to_register:
                if getattr(object, attribute) == getattr(temp, attribute):
                    return False
        return True
    
class Register:
    def register(to_register, __model__, attribute):
        if to_register:
            with transaction.atomic():                
                __model__.objects.bulk_create(to_register)
                
                for temp in to_register:
                    print(f'O item {getattr(temp, attribute)} foi cadastrado no banco de dados')
                        
            return True
        else: 
            return False