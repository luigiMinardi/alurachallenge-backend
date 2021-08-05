from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from collections import OrderedDict

from obeflix_back.models import Categoria


class CategoriaTestCase(APITestCase):

    def setUp(self):
        """
        Variaveis base pra ser usada em TODO teste
        """
        """
            // ? = doubt / ! = not using / * = using 
            ?url
            ?categoria
            ?response
        """
        self.url = reverse('Categorias-list')
        self.categoria = {
            "titulo": "LIVRE",
            "cor": "#000"
        }
        self.response = self.client.post(self.url,self.categoria, format='json')

        

    def test_if_data_is_valid_return_the_created_categoria_and_201(self):
        """
        (CATEGORIA-POST) Se os dados são válidos, retorne a categoria criada em um json e 201.
        """

        expected_response = {
          "id": 1,
          "titulo": "LIVRE",
          "cor": "#000"
        }

        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Categoria.objects.filter(titulo__iexact=f'LIVRE').count(), 1)
        self.assertEqual(self.response.data, expected_response)

    def test_when_changing_all_values_return_a_json_with_values_and_200(self):
        """
        (CATEGORIA-PUT) Quando troncando todos os dados, retorne um json com os dados e 200.
        """

        novos_dados = {
            "titulo": "LIVRE",
            "cor": "#fff"
        }

        expected_response = {
          "id": 1,
          "titulo": "LIVRE",
          "cor": "#fff"
        }
        response = self.client.put('/categorias/1/', novos_dados, format='json', follow=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_response)
    
    def test_when_changing_one_value_return_a_json_with_values_and_200(self):
        """
        (CATEGORIA-PATCH) Quando trocando um dado, retorne um json com os dados e 200.
        """

        novos_dados = {
            "cor": "#858585"
        }

        expected_response = {
          "id": 1,
          "titulo": "LIVRE",
          "cor": "#858585"
        }

        response = self.client.patch('/categorias/1/', novos_dados, format='json', follow=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_response)

    def test_when_deleting_a_categoria_return_a_json_of_success_and_200(self):
        """
        (CATEGORIA-DELETE) Quando deletando uma categoria retorne um json de sucesso e 200.
        """

        self.client.post(self.url,self.categoria, format='json')
      
        expected_response = {"detail": "Categoria deletada com sucesso!"}
        response = self.client.delete('/categorias/2/', follow=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_response)
    
    def test_when_getting_a_categoria_return_a_json_with_the_categoria_and_200(self):
        """
        (CATEGORIA-GET-ONE) Quando prucurando uma categoria retorne um json com a categoria e 200.
        """

        expected_response = {
          "id": 1,
          "titulo": "LIVRE",
          "cor": "#000"
        }

        response = self.client.get("/categorias/1/")
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_response)

    def test_when_getting_all_categorias_return_a_json_with_all_categorias_and_200(self):
        """
        (CATEGORIA-GET-ALL) Quando procurando todas as categorias retorne um json com todas as categorias e 200.
        """

        categoria_2 = {
          "titulo": "Livros",
          "cor": "#858585"
        }
        self.client.post(self.url, categoria_2, format='json')

        expected_response = [
          OrderedDict([('id', 1), ('titulo', 'LIVRE'), ('cor', '#000')]), 
          OrderedDict([('id', 2), ('titulo', 'Livros'), ('cor', '#858585')])
        ]

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_response)

    def test_when_changing_all_values_has_an_exception_return_a_custom_json_error_and_400(self):
        """
        (CATEGORIA-ERROR-PUT) Quando temos um erro ao alterar todos os dados de uma categoria retorne um erro customizado e 400. 
        """

        novos_dados = {
          "titulo": "LIVRE",
          "cor": "#85858"
        }

        expected_response = {
          "cor": [
            "Cor inválida!"
          ]
        }
        
        response = self.client.put('/categorias/1/',novos_dados,format='json',follow=True)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, expected_response)
    
    def test_when_changing_one_value_has_an_exception_return_a_custom_json_error_and_400(self):
        """
        (CATEGORIA-ERROR-PATCH) Quando temos um erro ao alterar um dado de uma categoria retorne um erro customizado e 400. 
        """

        novos_dados = {
          "titulo": "1234567890123456789012345678901",
        }

        expected_response = {
            'titulo': ['Titulo só pode ter 30 caracteres!'], 
        }
        response = self.client.patch('/categorias/1/',novos_dados,format='json',follow=True)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, expected_response)

    def test_when_deleting_the_first_categoria_return_a_json_custom_error_and_405(self):
        """
        (CATEGORIA-ERROR-DELETE-FIRST) Quando deletando a primeira categoria retorne um json de erro customizado e 205.
        """
      
        expected_response = {'detail': 'Você não pode deletar a categoria 1.'}
        response = self.client.delete('/categorias/1/', follow=True)

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(response.data, expected_response)

class NotFoundErrorCategoriaTestCase(APITestCase):
  
    def test_when_deleting_an_inexistent_categoria_return_a_json__custom_error_and_404(self):
        """
        (CATEGORIA-ERROR-DELETE) Quando deletando uma categoria inexistente retorno um erro customizado e 404.
        """

        expected_response = {'detail': 'Categoria não encontrada.'}
        response = self.client.delete('/categorias/2/', follow=True)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data, expected_response)

    def test_when_getting_an_inexistent_Categoria_return_a_json_custom_error_and_404(self):
        """
        (CATEGORIA-ERROR-GET-ONE) Ao pegar uma categoria inexistente retorne um erro customizado e 404.
        """

        expected_response = {'detail': 'Categoria não encontrada.'}
        response = self.client.get('/categorias/2/')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data, expected_response)

    def test_when_patching_an_inexistent_Categoria_return_a_json_custom_error_and_404(self):
        """
        (CATEGORIA-ERROR-PATCH) Quando alterando uma informação específica de uma categoria inexistente retorne um erro customizado e 404.
        """

        novos_dados = {
          "titulo": "1234567890123456789012345678901",
        }

        expected_response = {'detail': 'Categoria não encontrada.'}
        response = self.client.patch('/categorias/2/', novos_dados, format="json", follow=True)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data, expected_response)

    def test_when_changing_value_in_an_inexistent_Categoria_return_a__custom_not_found_json_error_and_404(self):
        """
        (CATEGORIA-ERROR-PUT) Quando alterando as informações de um Categoria inexistente retorne um erro customizado e 404.
        """

        novos_dados = {
          "titulo": "LIVRE",
          "cor": "#85858"
        }

        expected_response = {'detail': 'Categoria não encontrada.'}
        response = self.client.put('/categorias/2/', novos_dados, format='json', follow=True)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data, expected_response)

