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
