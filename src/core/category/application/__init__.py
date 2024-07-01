"""
Em applicattion é inserido os casos de uso, que são as regras de negócio da aplicação.
Desta forma a aplicação chama as entidades, nunca ao contrário. 
Os casos de uso podem ser por exemplo:
 

 [---->
                             [---->      
    Devices                                         [---->
    DB                              Controllers     
    External Interfaces             Geteways            User Case   ----> [Entities]    
    UI                              Presenters          
    WEB                                             [---->               
                             ]---->
 ]---->
 

 [User Case]
    + Create
    + List
    + Delete
    + Get
    + Update
"""