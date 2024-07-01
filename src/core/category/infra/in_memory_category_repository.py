from src.core.category.application.i_category_repository import CategoryRepository


class InMemoreyCategoryRepository(CategoryRepository):
    def __init__(self, categories = None):
        self.categories = categories or []

    def save(self, category):
        self.categories.append(category)