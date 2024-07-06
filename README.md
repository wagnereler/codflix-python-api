# codflix-python-api


Administracão de Catátogo
— Codeflix -
 ## Regras Category
    - [x] Nome da eategoria deverá ser obrigatório.
    - [x] Nome deverá ter no máximo 255 caracteres.
    - [x] AO criar uma nova Categoria um identificador deve ser gerado no formato (uuid).
    - [x] Ao criar uma categoria os campos id, descricäo e isActive näo seräo obrigatórios.
    - [x] Caso a propriedade isActive näo seja informada, deverá receber como default o valor

## Detalhes do projeto
Este projeto foi desenvolvido em arquitetura Clena Code utilizando DDD (Domain-driven design) e (Test Driven Development) 
Inicalmente forma contruídos os teses e as camadas mais interans da aplicação conforme abaixo:

 [---->
                             [---->      
    Devices                                         [---->
    DB                              Controllers     
    External Interfaces             Geteways            User Case   ----> [Entities]    
    UI                              Presenters          
    WEB                                             [---->               
                             ]---->
 ]---->

Foram criados as entidades em seguida os casos de susos, sem se preocular com o framework a ser utlizado,
uma vez que, no DDD e Clera Code se preza do desacoplamento (independência) das camadas.
Após a implementação incial foi escolhido o framework Django para costrução da API.

## Inclusão do framework Django 5.x
No Ubunto foi nessesário o seguinte procedimento:

sudo apt-get install libsqlite3-dev
pyenv uninstall 3.12.4
pyenv install 3.12.4
sem seguida pode sexecutar o comanto para inicializar o projeto:

# Para inicar o projeto
Rodar no terminal "django-admin startproject django_api src"

* Mover o arquivo manage.py para a raiz do projeto  e 
 Incluir sys.path.append('src') na primeria linha do método main() 
 caso isso não seja feito o Django não encontrará os arquivos de forma correta

* Modificar o arquivo setup.py:
* adicionar .parent.parent para que o django crie a database na raiz do projeto
  BASE_DIR = Path(__file__).resolve().parent.parent.parent

## Criando um Django APP
Será necessário criar um Django APP para cada domínio da aplicação
* Criar um diretório com o nome do app dentro do módulo src/django_api 
* Rodar o comando "python manage.py startapp cateogry_app ./src/django_api/category_app/" onde category_app é o meu módulo
* Dentro de setup.py, na lista INSTALLED_APPS incluir 'django_api.category_app', e todos os outros domínos da nossa aplicação.
* Dentro de src/django_api/category_app/apps.py alterar variável name para "name = 'django_api.cateogry_app'" 

## Comandos básicos
* python manage.py startapp cateogry_app ./src/django_api/category_app/ #cria um novo app
* django-admin startproject django_api #cria um novo projeto Django
* python manage.py runserver #starta o server
* python manage.py migrate # roda um migrate para sincronizar o ORM com o Bando de Dados

