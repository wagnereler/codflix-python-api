from dataclasses import dataclass
from uuid import UUID

from src.core.category.application.exceptions import CategoryNotFound
from src.core.category.application.i_category_repository import CategoryRepository



@dataclass
class UpdateCategoryRequest:
    id: UUID
    name: str | None = None
    description: str | None = None
    is_active: bool | None= None

class UpdateCategory:

        
    def __init__(self, repository: CategoryRepository):
        self.repository = repository
    def execute(self, request: UpdateCategoryRequest) -> None:
        category = self.repository.get_by_id(request.id)
        if category is None:
            raise CategoryNotFound
        else:
            # será utilizado o método category.update_category para atualizar os atributos
            # para isso será preciso tratar os atributos que podem ser nulos
            # para isso iremos utilizar o operador ternaário
            # https://docs.python.org/3/reference/expressions.html#conditional-expressions
            # https://realpython.com/python-ternary-operator/

            current_name = request.name if request.name is not None else category.name
            current_description = request.description if request.description is not None else category.description
            current_is_active = request.is_active if request.is_active is not None else category.is_active

            category.update_category(name=current_name, description=current_description)

            if current_is_active is True:
                category.activate()
            elif current_is_active is False:
                category.desactivate()

            self.repository.update(category)
            