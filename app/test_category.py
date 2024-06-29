from unittest import TestCase, main
from uuid import UUID
from category import Category

class TestCategory(TestCase):

    def test_name_is_required(self):
        with self.assertRaisesRegex(TypeError, "missing 1 required positional argument: 'name'"):
            Category()
    
    def test_name_must_have_lesas_then_255_characters(self):
        with self.assertRaisesRegex(ValueError, "name must have less then 256 characters"):
            Category(name='a' * 256)

    def test_category_uuid(self):
        category = Category(name='Filme')
        self.assertEqual(type(category.id), UUID)

    def test_category_defoult_values(self):
        category = Category(name='Filme')
        self.assertEqual(category.name, 'Filme')
        self.assertEqual(category.description, '' or None)

    def test_category_defoult_is_active_true(self):
        category = Category(name='Filme')
        self.assertEqual(category.is_active, True)
if __name__ == "__main__":
    main()
