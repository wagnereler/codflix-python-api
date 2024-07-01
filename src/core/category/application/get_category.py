from dataclasses import dataclass
from uuid import UUID
from src.core.category.application.i_category_repository import CategoryRepository
from src.core.category.application.exceptions import CategoryNotFound, InvalidCategoryData
from src.core.category.domain.category import Category


@dataclass
class GetCategoryRequest:
    id: UUID

@dataclass
class GetCategoryResponse:
    id: UUID
    name: str
    description: str
    is_active: bool

class GetCategory:

    def __init__(self, repository: CategoryRepository) -> None:
        self.repository = repository

    def execute(self, request: GetCategoryRequest) -> GetCategoryResponse:
        try:
            category = self.repository.get_by_id(request.id)
            if not category:
                raise CategoryNotFound(f'Category with {request.id} not found')
        except ValueError as error:
            raise CategoryNotFound(error)
        self.repository.save(category)
        
        return GetCategoryResponse(
            id = category.id,
            name = category.name,
            description = category.description,
            is_active = category.is_active
        )