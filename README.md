# Store


# pipenv shell
# pipenv install
# python manage.py runserver


## .env  --Database settings
```

DB_HOST=
DB_PORT=
DB_USER=
DB_PASSWORD=
DB_NAME=

```


# Como configurar 

## 1 -  Instalar o Apache Lounge e o Visual C++ Redistributable Visual Studio
### https://www.apachelounge.com/download/


## 2 - Colocar a pasta Apache24 no C:\


## 3 - No CMD com Admin entrar na pasta 'C:\Apache24\bin>' e executar 'httpd.exe -k install'


## 4 - Nas variaveis de ambiente colocar na variavel de usuario 'C:\Apache\bin' e na variavel de ambiente'MOD_WSGI_APACHE_ROOT_DIR C:\Apache24'


## 5 - No terminal do projeto executar 'mod_wsgi-express module-config' *Necessário o Visual Studio Community com o módulo de desenvolvimento de C++*
### Será devolvido pelo terminal três linhas (SALVE)
    
    
#### LoadFile "C:/Users/Nome_do_user/AppData/Local/Programs/Python/Python311/python311.dll"
#### LoadModule wsgi_module "C:/Users/Nome_do_user/.virtualenvs/Store-xMSCZ5t0/Lib/site-packages/mod_wsgi/server/mod_wsgi.cp311-win_amd64.pyd"
#### WSGIPythonHome "C:/Users/Nome_do_user/.virtualenvs/Store-xMSCZ5t0"


## 6 - Dentro da pasta Apache24 entre na pasta conf e no arquivo httpd.conf coloque os sequintes comandos mudando para suas configurações e pasta do seu ambiente
```

LoadFile "C:/Users/Nome_do_user/AppData/Local/Programs/Python/Python311/python311.dll"
LoadModule wsgi_module "C:/Users/Nome_do_user/.virtualenvs/Store-xMSCZ5t0/Lib/site-packages/mod_wsgi/server/mod_wsgi.cp311-win_amd64.pyd"
WSGIPythonHome "C:/Users/Nome_do_user/.virtualenvs/Store-xMSCZ5t0"

<VirtualHost *:80>

ServerName localhost

ServerAlias localhost

WSGIScriptAlias / "C:/Users/Nome_do_user/Documents/Store/project/wsgi.py"


<Directory "C:/Users/Nome_do_user/Documents/Store/project">

<Files wsgi.py>

Require all granted

</Files>

</Directory>

Alias /static "C:/Users/Nome_do_user/Documents/Store/global/static"

<Directory "C:/Users/Nome_do_user/Documents/Store/global/static">

Require all granted

</Directory>

</VirtualHost>


```

## 7 - No cmd novamente execute ipconfig e na linha do endereço IPv4 pegue o endereço que será colocado 
## no ALLOWED_HOSTS = ["localhost","*","127.0.0.1", "192.168.0.36"]  *O endereço pode variar*
### Endereço IPv4. . . . . . . .  . . . . . . . : 192.168.0.36


## 8 - Execute no CMD com Admin na pasta 'C:\Apache24\bin>' 'httpd.exe -k start' para iniciar o servidor e entrar no site pelo endereço que foi colocado no ALLOWED_HOSTS


## 9 - É necessario instalar o MySQL e configurar suas credenciais no .env
### Instale o MySQL Installer e Baixe o MySQL Server e configure, MySQL Workbench, MySQL Shell e MySQL Router 