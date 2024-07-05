from unittest.mock import create_autospec
from src.core.category.application.list_categories import CategoryOutput, ListCategories, ListCategoriesRequest, ListCategoriesResponse
from src.core.category.application.i_category_repository import CategoryRepository
from src.core.category.domain.category import Category
from src.core.category.infra.in_memory_category_repository import InMemoryCategoryRepository
from src.core.category.tests.domain.test_category import TestCategory


class TestListCategories:
    def test_when_repository_is_empty(self):
        category = Category(
            name="Filme",
            description="Filmes em geral"
        )

        repository = InMemoryCategoryRepository(categories=[])

        use_case = ListCategories(repository=repository)
        resquest = ListCategoriesRequest()
        response = use_case.execute(request=resquest)
        assert response == ListCategoriesResponse(data=[])

    def test_list_all_categories(self):
        categories = [
            Category(name="Filme", description="Filmes em geral"),
            Category(name="Séries", description="Séries em geral"),
            Category(name="Anime", description="Animes em geral"),]

        use_case = ListCategories(repository=InMemoryCategoryRepository(categories=categories))
        resquest = ListCategoriesRequest()
        response = use_case.execute(request=resquest)


        assert response == ListCategoriesResponse(data=[          
            CategoryOutput(
                id=category.id,
                name=category.name,
                description=category.description,
                is_active=category.is_active
            ) for category in categories
        ]
        )
