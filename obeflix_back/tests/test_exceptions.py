from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from uuid import uuid1


class ExceptionTestCase(APITestCase):

    def setUp(self):
        """
        Variaveis base pra ser usada em TODO teste
        """
        """
            // ? = doubt / * = using / ! = not using
            ?url
            ?uuid
            ?data
        """
        self.url = reverse('Videos-list')
        self.uuid = uuid1()
        self.data = {
            "titulo":"Teste",
            "descricao":f"{self.uuid.int}",
            "url":"http://blank.page"
        }

    def test_if_any_data_is_blank_return_return_a_custom_blank_json_error_and_400(self):
        """
        (ERROR-BLANK) Se algum dado estiver vazio retorne um json com o erro de onde estiver vazio e 400.
        """
        """
            *url
            *uuid
            *data
        """
        self.data["url"] = ""
        
        expected_response = {"url":["Url está em branco, por favor preencha corretamente."]}
        response = self.client.post(self.url, self.data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, expected_response)

    def test_if_any_data_has_more_length_than_the_max_return_a_custom_length_json_error_and_400(self):
        """
        (ERROR-MAX_LENGTH) Se algum dado exceder o tamanho retorne um json com o erro de tamanho e 400.
        """
        """
            *url
            *uuid
            *data
        """
        self.data["titulo"] = "1234567890123456789012345678901"

        expected_response = {'titulo': ['Titulo só pode ter 30 caracteres!']}
        response = self.client.post(self.url, self.data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, expected_response)

    def test_if_any_data_has_invalid_type_return_a_custom_invalid_json_error_and_400(self):
        """
        (ERROR-INVALID) Se algum dado for inválido retorne um json com o erro de dado invalido e 400.
        """
        """
            *url
            *uuid
            *data
        """
        self.data["url"] = "blank.page"

        expected_response = {'url': ['Url inválida!']}
        response = self.client.post(self.url, self.data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, expected_response)

class NotFoundErrorExceptionTestCase(APITestCase):

    def test_when_not_finding_a_video_return_a_json_custom_error_and_404(self):
        """
        (ERROR-NOT-FOUND-VIDEO) Se tentar pegar um video inexistente retorne um json com o erro de Video não encontrado e 404.
        """

        expected_response = {'detail': 'Vídeo não encontrado.'}
        response = self.client.get('/videos/2/')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data, expected_response)

    def test_when_not_finding_a_category_return_a_json_custom_error_and_404(self):
        """
        (ERROR-NOT-FOUND-CATEGORIA) Se tentar pegar uma categoria inexistente retorne um json com o erro de Categoria não encontrada e 404.
        """

        expected_response = {'detail': 'Categoria não encontrada.'}
        response = self.client.get('/categorias/2/')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data, expected_response)