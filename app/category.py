from uuid import uuid4 as uuid
class Category:
    def __init__(self,
                 name,
                 id = None,
                 description = None,
                 is_active = True ) -> None:
        self.id = id or uuid()
        self.name = name
        self.description = description
        self.is_active = is_active

        if len(self.name) > 255:
            raise ValueError('name must have less then 256 characters')
    def __str__(self) -> str:
        return f' id: {id} nome: {self.name} \ndescrição: {self.description} \nativo: {self.is_active}'
    
    def __repr__(self) -> str:
        return  f' id: {id} nome: {self.name} \ndescrição: {self.description} \nativo: {self.is_active}'
