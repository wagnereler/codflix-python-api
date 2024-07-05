from uuid import uuid4
from src.core.category.application.detele_category import DeleteCategory, DeleteCategoryRequest
from src.core.category.domain.category import Category
from src.core.category.infra.in_memory_category_repository import InMemoryCategoryRepository


class TestDeleteCategory:
    def test_delete_category_from_repository(self):
        category_filme = Category(
            id = uuid4(),
            name = 'Filme',
            description = 'Categoria para filmes',
            is_active=True
        )
        category_serie = Category(
            id = uuid4(),
            name = 'Série',
            description = 'Categoria para séries',
            is_active=True
        )

        repository = InMemoryCategoryRepository(
            categories = [
                category_filme, 
                category_serie,
                ]
        )
        use_case = DeleteCategory(repository = repository)
        request = DeleteCategoryRequest(id = category_filme.id)

        assert repository.get_by_id(category_filme.id) != None   
        response = use_case.execute(request)
        
        assert repository.get_by_id(category_filme.id) == None
        assert response == None
        