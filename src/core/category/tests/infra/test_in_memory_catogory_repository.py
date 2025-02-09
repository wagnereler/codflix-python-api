from src.core.category.domain.category import Category
from src.core.category.infra.in_memory_category_repository import InMemoryCategoryRepository


class TestInMemoryCatetoryRepository:
    def test_can_save_category(self):
        repository = InMemoryCategoryRepository()
        category = Category(
            name = 'Filme',
            description = 'Categoria para filmes'
        )

        repository.save(category)

        assert len(repository.categories) == 1
        assert repository.categories[0] == category

    def test_can_get_by_id(self):
        repository = InMemoryCategoryRepository()
        category = Category(
            name = 'Filme',
            description = 'Categoria para filmes'
        )

        repository.save(category)

        assert repository.get_by_id(category.id) == category