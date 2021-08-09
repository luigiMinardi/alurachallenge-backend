from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from uuid import uuid1
from collections import OrderedDict

from obeflix_back.models import Video


class VideoTestCase(APITestCase):

    def setUp(self):
        """
        Variaveis base pra ser usada em TODO teste
        """
        """
            // ? = doubt / ! = not using / * = using 
            ?url
            ?uuid
            ?data
            ?response
        """
        self.url = reverse('Videos-list')
        self.uuid = uuid1()
        self.data = {
            "titulo":"Teste",
            "descricao":f"{self.uuid.int}",
            "url":"http://blank.page"
        }
        self.categoria_1 = {
            "titulo": "teste",
            "cor": "#000"
        }
        self.response = self.client.post(self.url, self.data, format='json')

        self.client.post('/categorias/',self.categoria_1, format='json')

    def test_if_data_is_valid_return_the_created_video_and_201(self):
        """
        (VIDEO-POST) Se os dados são válidos, retorne o video criado em um json e 201.
        """

        expected_response = {'id': 1, 'titulo': 'Teste', 'descricao': f'{self.uuid.int}', 'url': 'http://blank.page', 'categoriaId': 1}

        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Video.objects.filter(descricao__iexact=f'{self.uuid.int}').count(), 1)
        self.assertEqual(self.response.data, expected_response)

    def test_when_changing_all_values_return_a_json_with_values_and_200(self):
        """
        (VIDEO-PUT) Quando trocando todos os dados, retorne um json com os dados e 200.
        """

        categoria_2 = {
            "titulo": "teste",
            "cor": "#000"
        }

        self.client.post('/categorias/',categoria_2, format='json')
        
        data2 = {
            "titulo": "Teste2",
            "descricao": f"{self.uuid.hex}",
            "url": "http://blank.page",
            'categoriaId': 2
        }

        expected_response = {"id":1,"titulo":"Teste2","descricao":f"{self.uuid.hex}","url":"http://blank.page","categoriaId": 2}

        response = self.client.put('/videos/1/',data2, format='json', follow=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_response)
    
    def test_when_changing_one_value_return_a_json_with_values_and_200(self):
        """
        (VIDEO-PATCH) Quando trocando um dado, retorne um json com os dados e 200.
        """

        data2 = {
            "url": "https://randompage.net/"
        }

        expected_response = {"id":1,"titulo":"Teste","descricao":f"{self.uuid.int}","url":"https://randompage.net/",'categoriaId': 1}
        response = self.client.patch('/videos/1/',data2, format='json', follow=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_response)

    def test_when_deleting_a_video_return_a_json_of_success_and_200(self):
        """
        (VIDEO-DELETE) Quando deletando um video retorne um json de sucesso e 200.
        """

        expected_response = {"detail": "Vídeo deletado com sucesso!"}
        response = self.client.delete('/videos/1/', follow=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_response)
    
    def test_when_getting_a_video_return_a_json_with_the_video_and_200(self):
        """
        (VIDEO-GET-ONE) Quando prucurando um video retorne um json com o video e 200.
        """

        expected_response = {"id":1,"titulo":"Teste","descricao":f"{self.uuid.int}","url":"http://blank.page",'categoriaId': 1}
        response = self.client.get("/videos/1/")
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_response)

    def test_when_getting_all_videos_return_a_json_with_all_videos_and_200(self):
        """
        (VIDEO-GET-ALL) Quando procurando todos os videos retorne um json com todos os videos e 200.
        """

        data2 = {
            "titulo": "Teste2",
            "descricao": f"{self.uuid.hex}",
            "url": "http://blank.page",
        }
        self.client.post(self.url, data2, format='json')

        expected_response = [
            OrderedDict([('id', 1), ('titulo', 'Teste'), ('descricao', f"{self.uuid.int}"), ('url', 'http://blank.page'), ('categoriaId', 1)]), 
            OrderedDict([('id', 2), ('titulo', 'Teste2'), ('descricao', f"{self.uuid.hex}"), ('url', 'http://blank.page'), ('categoriaId', 1)])
        ]

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_response)
    
    def test_when_getting_searched_videos_return_a_json_with_all_matched_seached_videos_and_200(self):
        """
        (VIDEO-GET-SEARCH) Quando pesquisando videos retorne um json com todos os videos relativos a pesquisa e 200.
        """

        data2 = {
            "titulo": "Abacate",
            "descricao": f"{self.uuid.hex}",
            "url": "http://blank.page",
        }
        self.client.post(self.url, data2, format='json')

        expected_response = [
            OrderedDict([('id', 2), ('titulo', 'Abacate'), ('descricao', f"{self.uuid.hex}"), ('url', 'http://blank.page'), ('categoriaId', 1)])
        ]

        response = self.client.get('/videos/?search=abacate')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_response)

    def test_when_changing_all_values_has_an_exception_return_a_custom_json_error_and_400(self):
        """
        (VIDEO-ERROR-PUT) Quando temos um erro ao alterar todos os dados de um video retorne um erro customizado e 400. 
        """

        data2 = {
            "titulo": "Teste2",
            "descricao": f"{self.uuid.hex}",
            "url": "123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901"
        }

        expected_response = {'url': ['Url só pode ter 200 caracteres!','Url inválida!']}
        response = self.client.put('/videos/1/',data2,format='json',follow=True)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, expected_response)
    
    def test_when_changing_one_value_has_an_exception_return_a_custom_json_error_and_400(self):
        """
        (VIDEO-ERROR-PATCH) Quando temos um erro ao alterar um dado de um video retorne um erro customizado e 400. 
        """

        data2 = {
            "descricao": "",
            "titulo": ""
        }

        expected_response = {
            'titulo': ['Titulo está em branco, por favor preencha corretamente.'], 
            'descricao': ['Descricao está em branco, por favor preencha corretamente.']
        }
        response = self.client.patch('/videos/1/',data2,format='json',follow=True)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, expected_response)


class NotFoundErrorVideoTestCase(APITestCase):

    def test_when_deleting_an_inexistent_video_return_a_json__custom_error_and_404(self):
        """
        (VIDEO-ERROR-DELETE) Quando deletando um video inexistente retorno um erro customizado e 404.
        """

        expected_response = {'detail': 'Vídeo não encontrado.'}
        response = self.client.delete('/videos/2/', follow=True)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data, expected_response)

    def test_when_getting_an_inexistent_video_return_a_json_custom_error_and_404(self):
        """
        (VIDEO-ERROR-GET-ONE) Ao pegar um video inexistente retorne um erro customizado e 404.
        """

        expected_response = {'detail': 'Vídeo não encontrado.'}
        response = self.client.get('/videos/2/')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data, expected_response)

    def test_when_patching_an_inexistent_video_return_a_json_custom_error_and_404(self):
        """
        (VIDEO-ERROR-PATCH) Quando alterando uma informação específica de um video inexistente retorne um erro customizado e 404.
        """

        data2 = {
            "url": "https://randompage.net/"
        }

        expected_response = {'detail': 'Vídeo não encontrado.'}
        response = self.client.patch('/videos/2/', data2, format="json", follow=True)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data, expected_response)

    def test_when_changing_value_in_an_inexistent_video_return_a__custom_not_found_json_error_and_404(self):
        """
        (VIDEO-ERROR-PUT) Quando alterando as informações de um video inexistente retorne um erro customizado e 404.
        """

        data = {
            "titulo":"Teste",
            "descricao":"testando",
            "url":"http://blank.page"
        }

        expected_response = {'detail': 'Vídeo não encontrado.'}
        response = self.client.put('/videos/2/', data, format='json', follow=True)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data, expected_response)