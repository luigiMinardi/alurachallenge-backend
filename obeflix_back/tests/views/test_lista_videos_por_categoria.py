from rest_framework.test import APITestCase
from rest_framework import status
from collections import OrderedDict

class ListaVideosPorCategoriaTestCase(APITestCase):

    def setUp(self):
        """
        Variaveis base pra ser usada em TODO teste
        """
        """
            // ? = doubt / ! = not using / * = using 
            ?categoria
            ?categoria_2
            ?data
            ?data_2
        """
        self.categoria = {
            "titulo": "LIVRE",
            "cor": "#000"
        }
        self.categoria_2 = {
            "titulo": "Livros",
            "cor": "#858585"
            }
        self.data = {
            "titulo":"Teste data 1",
            "descricao": "testando data 1",
            "url":"http://blank.page",
        }
        self.data_2 = {
            "titulo":"Teste data 2",
            "descricao": "testando data 2",
            "url":"http://blank.page",
            "categoriaId": 2
        }
        self.client.post('/categorias/',self.categoria, format='json')
        self.client.post('/categorias/',self.categoria_2, format='json')
        self.client.post('/videos/', self.data, format='json')
        self.client.post('/videos/', self.data_2, format='json')

    def test_when_getting_all_videos_from_one_categoria_return_a_json_with_the_videos_from_the_specified_categoria_and_200(self):
            """
            (VIDEOS_POR_CATEGORIA-GET) Quando procurando todos os videos de uma categoria retorne um json com todos os videos dessa categoria e 200.
            """
            self.data = {
            "titulo":"Abacate",
            "descricao": "abacateiro",
            "url":"http://blank.page",
            }
            self.client.post('/videos/', self.data, format='json')

            expected_response = [
                OrderedDict([('id', 1), ('titulo', 'Teste data 1'), ('descricao', 'testando data 1'), ('url', 'http://blank.page'), ('categoriaId', 1)]), 
                OrderedDict([('id', 3), ('titulo', 'Abacate'), ('descricao', 'abacateiro'), ('url', 'http://blank.page'), ('categoriaId', 1)])
            ]

            response = self.client.get('/categorias/1/videos/')
            
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(response.data, expected_response)
    
    def test_when_getting_searched_videos_from_one_categoria_return_a_json_with_the_searched_video_and_200(self):
            """
            (VIDEOS_POR_CATEGORIA-GET-SEARCH) Quando procurando videos específicos de uma categoria 
            retorne um json com todos os videos resultantes da procura que estejam nessa categoria e 200.
            """
            self.data = {
            "titulo":"Abacate",
            "descricao": "abacateiro",
            "url":"http://blank.page",
            }
            self.client.post('/videos/', self.data, format='json')

            expected_response = [
                OrderedDict([('id', 3), ('titulo', 'Abacate'), ('descricao', 'abacateiro'), ('url', 'http://blank.page'), ('categoriaId', 1)])
            ]

            response = self.client.get('/categorias/1/videos/?search=abacate')

            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(response.data, expected_response)