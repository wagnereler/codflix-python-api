from rest_framework.test import APITestCase

class TestCategoryAPI(APITestCase):
    def test_list_categories(self):
        uri = '/api/categories/'
        response = self.client.get(uri)
        excepcted_data = [
            {
                'id': '9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d',
                'name': 'Filme',
                'description': 'Filmes em geral',
                'is_active': True
            },
            {
                'id': '6f1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d',
                'name': 'Séries',
                'description': 'Séries em geral',
                'is_active': True
            }
        ]
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, excepcted_data)

        #para rodar o teste executar a linha abaixo
        #python manage.py test jango_api.category_app
