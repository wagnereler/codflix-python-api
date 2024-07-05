from unittest.mock import create_autospec
from uuid import uuid4
from src.core.category.application.i_category_repository import CategoryRepository
from src.core.category.application.update_category import UpdateCategory, UpdateCategoryRequest
from src.core.category.domain.category import Category


class TestUpdateCategory:
    def test_update_category_name(self):
        category = Category(
            id= uuid4(),
            name='Filme', 
            description='Filmes em geral', 
            is_active=True
            )  
        mock_repository = create_autospec(CategoryRepository)
        mock_repository.get_by_id.return_value = category

        use_case = UpdateCategory(repository=mock_repository)
        request = UpdateCategoryRequest(
            id = category.id,
            name = 'Série'
        )

        response = use_case.execute(request)
        mock_repository.update.assert_called_once_with(category)

        assert category.name == 'Série'
        assert category.description == 'Filmes em geral'
        # category.update.assert_called_once_with(category)

    def test_update_description(self):
        category = Category(
            id=uuid4(),
            name='Filme',
            description='Filmes em geral',
            is_active=True
        )
        mock_repository = create_autospec(CategoryRepository)
        mock_repository.get_by_id.return_value = category

        use_case = UpdateCategory(repository=mock_repository)
        request = UpdateCategoryRequest(
            id=category.id,
            description='Séries em geral'
        )

        response = use_case.execute(request)
        mock_repository.update.assert_called_once_with(category)

        assert category.description == 'Séries em geral'
        assert category.name == 'Filme'

    def test_update_category_activate(self):
        category = Category(
            id=uuid4(),
            is_active=False,
            name='Filme',
            description='Filmes em geral',
        )
        mock_repository = create_autospec(CategoryRepository)
        mock_repository.get_by_id.return_value = category

        use_case = UpdateCategory(repository=mock_repository)
        request = UpdateCategoryRequest(
            id=category.id,
            is_active=True
        )

        response = use_case.execute(request)
        mock_repository.update.assert_called_once_with(category)

        assert category.is_active is True

    def test_update_category_desactivate(self):
        category = Category(
            id=uuid4(),
            name='Filme',
            description='Filmes em geral',
            is_active=True
        )
        mock_repository = create_autospec(CategoryRepository)
        mock_repository.get_by_id.return_value = category

        use_case = UpdateCategory(repository=mock_repository)
        request = UpdateCategoryRequest(
            id=category.id,
            is_active=False
        )

        response = use_case.execute(request)
        mock_repository.update.assert_called_once_with(category)

        assert category.is_active is False