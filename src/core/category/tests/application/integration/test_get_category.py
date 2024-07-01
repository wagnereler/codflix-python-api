from uuid import UUID, uuid4

from pytest import raises
from src.core.category.application.exceptions import CategoryNotFound
from src.core.category.application.get_category import GetCategory, GetCategoryRequest, GetCategoryResponse
from src.core.category.domain.category import Category
from src.core.category.infra.in_memory_category_repository import InMemoreyCategoryRepository



class TestGetCategory:
    def test_get_category_by_id(self):
        category_filme = Category(
            name = 'Filme',
            description = 'Categoria para filmes'
        )
        category_serie = Category(
            name = 'Série',
            description = 'Categoria para séries'
        )

        repository = InMemoreyCategoryRepository(
            categories = [category_filme, category_serie]
        )
        use_case = GetCategory(repository = repository)

        request = GetCategoryRequest(
            id = category_filme.id
        )

        response = use_case.execute(request)

        assert response == GetCategoryResponse(
            id = category_filme.id,
            name = 'Filme',
            description = 'Categoria para filmes',
            is_active = True
        )

    def test_get_category_by_id_when_not_found(self):
        category_filme = Category(
            name = 'Filme',
            description = 'Categoria para filmes'
        )
        category_serie = Category(
            name = 'Série',
            description = 'Categoria para séries'
        )

        repository = InMemoreyCategoryRepository(
            categories = [category_filme, category_serie]
        )
        use_case = GetCategory(repository = repository)

        request = GetCategoryRequest(
            id = uuid4()
        )

        with raises(CategoryNotFound) as exc_info:
            use_case.execute(request)
        


    