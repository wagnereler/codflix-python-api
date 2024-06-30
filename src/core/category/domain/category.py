from dataclasses import dataclass, field
from uuid import UUID, uuid4 as uuid

@dataclass
class Category:
    name: str
    description: str = ''
    is_active: bool = True
    id: UUID = field(default_factory=uuid)

    def __post_init__(self):
        self.validate()

    # def __init__(self,
    #              name,
    #              id = None,
    #              description = "",
    #              is_active = True ) -> None:
    #     self.id = id or uuid()
    #     self.name = name
    #     self.description = description
    #     self.is_active = is_active

    #     self.validate()

    def validate(self) -> None:
        if len(self.name) > 255:
            raise ValueError('name cannot be loger then 255 characters')
        if not self.name:
            raise ValueError('name cannot be empty')
        
    def update_category(self, name, description) -> None:
        self.name = name
        self.description = description
        self.validate()

    def activate(self) -> None:
        self.is_active = True
        self.validate()

    def desactivate(self) -> None:
        self.is_active = False
        self.validate()

    def __str__(self) -> str:
        return f' id: {id} nome: {self.name} \ndescrição: {self.description} \nativo: {self.is_active}'
    
    def __repr__(self) -> str:
        return  f' id: {id} nome: {self.name} \ndescrição: {self.description} \nativo: {self.is_active}'

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Category):
            return False
        return self.id == value.id