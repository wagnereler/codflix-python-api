from unittest.mock import create_autospec

from pytest import raises
from src.core.category.application.detele_category import DeleteCategory, DeleteCategoryRequest
from src.core.category.application.exceptions import CategoryNotFound
from src.core.category.application.i_category_repository import CategoryRepository
from src.core.category.domain.category import Category


class TestDeleteCategory:
    def test_delete_category_from_repository(self):
        category = Category(
            name='Filme', 
            description='Filmes em geral')
        mock_repository = create_autospec(CategoryRepository)
        mock_repository.get_by_id.return_value = category
        
        use_case = DeleteCategory(mock_repository)
        use_case.execute(DeleteCategoryRequest(id=category.id))
        
        mock_repository.delete.assert_called_once_with(category.id)

    def test_when_category_not_found(self):
        mock_repository = create_autospec(CategoryRepository)
        mock_repository.get_by_id.return_value = None

        use_case = DeleteCategory(mock_repository)
        
        
        with raises(CategoryNotFound):
            use_case.execute(DeleteCategoryRequest(id='00000000-0000-0000-0000-000000000000'))

        mock_repository.delete.assert_not_called()
        assert mock_repository.delete.called is False