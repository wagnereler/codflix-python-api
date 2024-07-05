from unittest.mock import create_autospec
from uuid import uuid4

import pytest
from src.core.category.application.exceptions import CategoryNotFound
from src.core.category.application.i_category_repository import CategoryRepository
from src.core.category.application.update_category import UpdateCategory, UpdateCategoryRequest
from src.core.category.domain.category import Category
from src.core.category.infra.in_memory_category_repository import InMemoryCategoryRepository


class TestUdateCategory:
    def test_update_category_name(self):
        category = Category(
            name='Filme',
            description='Filmes em geral',
            is_active=True
        )

        repository = InMemoryCategoryRepository()
        repository.save(category)

        use_case = UpdateCategory(repository = repository)
        
        request = UpdateCategoryRequest(
            id=category.id,
            name='Séries',
            description='Filmes em geral',
        )

        use_case.execute(request)
        
        uploted_category = repository.get_by_id(category.id)
        assert uploted_category.name == 'Séries'
        assert uploted_category.description == 'Filmes em geral'

    def test_update_description(self):
        category = Category(
            name='Filme',
            description='Filmes em geral',
            is_active=True  
        )

        repository = InMemoryCategoryRepository()
        repository.save(category)

        use_case = UpdateCategory(repository = repository)
        
        request = UpdateCategoryRequest(
            id=category.id,
            description='Séries em geral'
        )

        use_case.execute(request)
        
        uploted_category = repository.get_by_id(category.id)
        assert uploted_category.description == 'Séries em geral'
        assert uploted_category.name == 'Filme'


    def test_update_category_activate(self):
        category = Category(
            name='Filme',
            description='Filmes em geral',
            is_active=True  
        )

        repository = InMemoryCategoryRepository()
        repository.save(category)

        use_case = UpdateCategory(repository = repository)
        
        request = UpdateCategoryRequest(
            id=category.id,
            is_active=False
        )

        use_case.execute(request)
        
        uploted_category = repository.get_by_id(category.id)
        assert uploted_category.is_active is False

    def test_update_category_with_invalid_id(self):
        category = Category(
            name='Filme',
            description='Filmes em geral',
            is_active=True  
        )

        repository =    InMemoryCategoryRepository()
        repository.save(category)

        use_case = UpdateCategory(repository = repository)
        
        request = UpdateCategoryRequest(
            id=uuid4(),
            name='Séries',
            description='Filmes em geral',
        )

        
        with pytest.raises(CategoryNotFound) as exc_info:
            ploted_category = repository.get_by_id(category.id)
            use_case.execute(request)
            
    def test_update_category_with_invalid_name(self):
        category = Category(
            name='Filme',
            description='Filmes em geral',
            is_active=True  
        )

        repository = InMemoryCategoryRepository()
        repository.save(category)

        use_case = UpdateCategory(repository = repository)
        
        request = UpdateCategoryRequest(
            id=category.id,
            name='a' * 300,
            description='Filmes em geral',
        )

        with pytest.raises(ValueError) as exc_info:
            use_case.execute(request)

        assert 'name cannot be loger then 255 characters' in str(exc_info.value)