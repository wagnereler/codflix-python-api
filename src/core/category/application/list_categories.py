from dataclasses import dataclass
from uuid import UUID
from src.core.category.application.i_category_repository import CategoryRepository
from src.core.category.domain.category import Category

@dataclass
class ListCategoriesRequest:
    pass

@dataclass
class CategoryOutput:
    id: UUID
    name: str
    description: str
    is_active: bool    

@dataclass
class ListCategoriesResponse:
    data: list[CategoryOutput]  

class ListCategories:

    def __init__(self, repository: CategoryRepository) -> None:
        self.repository = repository

    def execute(self, request: ListCategoriesRequest) -> ListCategoriesResponse:
        categories = self.repository.list_categories()

        return ListCategoriesResponse(
            # categories = list(map(lambda category: CategoryOutput(**category.__dict__), categories))
            # categories = [CategoryOutput(**category.__dict__) for category in categories]
            # categories = [CategoryOutput(**category) for category in categories]
            data = [
                CategoryOutput(
                    id = category.id,
                    name = category.name,
                    description = category.description,
                    is_active = category.is_active
                ) for category in categories
            ]
        )