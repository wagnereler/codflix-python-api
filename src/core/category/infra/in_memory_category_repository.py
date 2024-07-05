from uuid import UUID
from src.core.category.application.i_category_repository import CategoryRepository
from src.core.category.domain.category import Category


class InMemoryCategoryRepository(CategoryRepository):
    def __init__(self):
        self.categories = {}

    def save(self, category: Category) -> None:
        self.categories[category.id] = category

    def get_by_id(self, id: UUID) -> Category | None:
        return self.categories.get(id)

    def delete(self, id: UUID) -> None:
        del self.categories[id]

    def update(self, category: Category) -> None:
        if self.categories[category.id].name:
            self.categories[category.id].name = category.name
        if self.categories[category.id].description:
            self.categories[category.id].description = category.description
        if self.categories[category.id].is_active:    
            self.categories[category.id].is_active = category.is_active
