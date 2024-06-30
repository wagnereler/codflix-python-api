import pytest
from uuid import UUID
from src.core.category.domain.category import Category

class TestCategory:

    def test_name_is_required(self):
        with pytest.raises(TypeError, match="missing 1 required positional argument: 'name'"):
            Category()
    
    def test_name_must_have_lesas_then_255_characters(self):
        with pytest.raises(ValueError, match='name cannot be loger then 255 characters'):
            Category(name='a' * 300)

    def test_cannot_create_category_with_enpty_name(self):
        with pytest.raises(ValueError, match = 'name cannot be empty'):
            Category(name='')

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

class TestUpdateCategory:
    def test_update_category_with_name_end_description(self):
        category = Category(name='Filme', description='Filmes em geral')
        category.update_category(name='Séries', description='Séries em geral')

        assert category.name == 'Séries'
        assert category.description == 'Séries em geral'

    def test_update_category_name_lesas_then_255_characters(self):
        category = Category(name='Filme', description='Filmes em geral')
        with pytest.raises(ValueError, match='name cannot be loger then 255 characters'):
            category.update_category(name= 'a' * 300, description='Séries em geral')
    
    def test_cannot_update_category_name_with_enpty_name(self):
        category = Category(name='Filme', description='Filmes em geral')
        with pytest.raises(ValueError, match='name cannot be empty'):
            category.update_category(name= '', description='Séries em geral')


class TestActive:
    def test_activate_category(self):
        category = Category(name='Filme', description='Filmes em geral', is_active=False)
        category.activate()
        assert category.is_active is True            

    def test_activate_category_when_true(self):
        category = Category(name='Filme', description='Filmes em geral', is_active=True)
        category.activate()
        assert category.is_active is True        

class TestDesactive:
    def test_desactivate_category(self):
        category = Category(name='Filme', description='Filmes em geral', is_active=True)
        category.desactivate()
        assert category.is_active is False            

    def test_desactivate_category_when_false(self):
        category = Category(name='Filme', description='Filmes em geral', is_active=False)
        category.desactivate()
        assert category.is_active is False

class TestEquality:
    def test_when_categories_have_same_id_they_are_equal(self):
        cammon_id = UUID
        category_1 = Category(name='Filmes', id=cammon_id)
        category_2 = Category(name='Filmes', id=cammon_id)

        assert category_1 == category_2