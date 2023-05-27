from home import models

class getFromDatabase:
    class AboutSupplier():
        def getAll():
            return models.Fabricante.objects.all().order_by('nome')
        
        def getTotalNumberRegistered():
            return models.Fabricante.objects.count()
        
    class AboutCategory():
        def getAll():
            return models.Categoria.objects.all().order_by('nome')
        
        def getTotalNumberRegistered():
            return models.Categoria.objects.count()
        
    class AboutStorage():
        def getAll():
            return models.Armazem.objects.all().order_by('nome')
        
        def getTotalNumberRegistered():
            return models.Armazem.objects.count()
        
    class AboutComponent():
        def getAll():
            return models.Componente.objects.all().order_by('nome')
        
        def getTotalNumberRegistered():
            return models.Componente.objects.count()
        
    class AboutComputer():
        def getAll():
            return models.Computador.objects.all().order_by('nome')
        
        def getTotalNumberRegistered():
            return models.Computador.objects.count()
        

    
    
    class ifExists:
        def Computer(computer_id):
            client = models.Computador.objects.filter(nome = computer_id)
            return client
            
        def Client(client_id):
            client = models.Cliente.objects.filter(nome = client_id)
            return client
            
        def Supplier(supplier_id):
            supplier = models.Fabricante.objects.filter(nome = supplier_id)
            return supplier.exists()
