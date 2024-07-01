from unittest.mock import MagicMock, create_autospec
from uuid import UUID, uuid4

from pytest import raises
from src.core.category.application.exceptions import CategoryNotFound
from src.core.category.application.get_category import GetCategory, GetCategoryRequest, GetCategoryResponse
from src.core.category.application.i_category_repository import CategoryRepository
from src.core.category.domain.category import Category



class TestGetCategory:
    def test_get_category_by_id(self):
        category = Category(
            name = 'Filme',
            description = 'Categoria para filmes',
            is_active = True
        )
        mock_repository = create_autospec(CategoryRepository)
        mock_repository.get_by_id.return_value = category
        
        use_case = GetCategory(repository = mock_repository)
        request = GetCategoryRequest(
            id = category.id
        )

        response = use_case.execute(request)

        assert response == GetCategoryResponse(
            id = category.id,
            name = 'Filme',
            description = 'Categoria para filmes',
            is_active = True
        )


    