from uuid import UUID
from src.core.category.application.i_category_repository import CategoryRepository
from src.core.category.domain.category import Category


class InMemoreyCategoryRepository(CategoryRepository):
    def __init__(self, categories = None) -> None:
        self.categories = categories or []

    def save(self, category):
        self.categories.append(category)
    def get_by_id(self, category_id: UUID) -> Category | None:
        return next((category for category in self.categories if category.id == category_id), None)