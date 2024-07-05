from src.core.category.application.detele_category import DeleteCategory, DeleteCategoryRequest
from src.core.category.domain.category import Category
from src.core.category.infra.in_memory_category_repository import InMemoreyCategoryRepository


class TestDeleteCategory:
    def test_delete_category_from_repository(self):
        category_filme = Category(
            name = 'Filme',
            description = 'Categoria para filmes'
        )
        category_serie = Category(
            name = 'Série',
            description = 'Categoria para séries'
        )

        repository = InMemoreyCategoryRepository(
            categories = [
                category_filme, 
                category_serie]
        )
        use_case = DeleteCategory(repository = repository)
        request = DeleteCategoryRequest(id = category_filme.id)

        assert repository.get_by_id(category_filme.id) is not None   
        
        response = use_case.execute(request)
        
        assert repository.get_by_id(category_filme.id) is None  
        assert response is None
        assert len(repository.categories) == 1
        assert repository.categories[0] == category_serie