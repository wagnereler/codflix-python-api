from uuid import UUID
from src.core.category.application.i_category_repository import CategoryRepository
from src.core.category.domain.category import Category


class InMemoryCategoryRepository(CategoryRepository):
    def __init__(self, categories: list[Category]=None):
        self.categories: list[Category] = categories or []

    def save(self, category: Category) -> None:
        self.categories.append(category)

    def get_by_id(self, id: UUID) -> Category | None:
        return next(
            (category for category in self.categories if category.id == id), None
        )

    def delete(self, id: UUID) -> None:
        self.categories = [category for category in self.categories if category.id != id]

    def list_categories(self) -> list[Category]:
        return [category for category in self.categories]

    def update(self, category: Category) -> None:
        old_category = self.get_by_id(category.id)
        if old_category:
            self.categories.remove(old_category)
            self.categories.append(category)

    def list_categories(self) -> list[Category]:
        # O retorno é uma lista de categorias utilizando list comprehension
        return [cateogry for cateogry in self.categories]
