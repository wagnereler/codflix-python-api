from dataclasses import dataclass
from uuid import UUID
from src.core.category.application.i_category_repository import CategoryRepository
from src.core.category.application.exceptions import InvalidCategoryData
from src.core.category.domain.category import Category


@dataclass
class CreateCategoryRequest:
    name: str
    description: str = ''
    is_active: bool = True

@dataclass
class CreateCategoryResponse:
    id: UUID

class CreateCategory:

    def __init__(self, repository: CategoryRepository) -> None:
        self.repository = repository

    def execute(self, request: CreateCategoryRequest) -> CreateCategoryResponse:
        try:
            category = Category(
                name=request.name,
                description=request.description,
                is_active=request.is_active
            )
        except ValueError as error:
            raise InvalidCategoryData(error)
        self.repository.save(category)
        return CreateCategoryResponse(id = category.id)