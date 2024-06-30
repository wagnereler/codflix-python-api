import pytest
from uuid import UUID

from category import Category

class TestCategory:

    def test_name_is_required(self):
        with pytest.raises(TypeError, match="missing 1 required positional argument: 'name'"):
            Category()
    
    def test_name_must_have_lesas_then_255_characters(self):
        with pytest.raises(ValueError, match='name must have less then 256 characters'):
            Category(name='a' * 300)

    def test_category_uuid(self):
        category = Category(name='Filme')
        assert isinstance(category.id, UUID)

    def test_category_defoult_values(self):
        category = Category(name='Filme')
        assert category.name == 'Filme'
        assert category.description == ''

    def test_category_defoult_is_active_true(self):
        category = Category(name='Filme')
        assert category.is_active == True
