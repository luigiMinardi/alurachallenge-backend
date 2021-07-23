from django.http import response
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from uuid import uuid1

from obeflix_back.models import Video


class VideoTestCase(APITestCase):

    def setUp(self):
        """
        Variaveis base pra ser usada em TODO teste
        """
        """
            // ? = doubt / * = using / ! = not using
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
        self.response = self.client.post(self.url, self.data, format='json')


    def test_if_data_is_valid_create_a_video_and_return_201(self):
        """
        (POST) Se os dados são válidos cria um video, retorne os dados em um json e 201.
        """
        """
            *url
            *uuid
            *data
            *response
        """
        expected_response = {'id': 1, 'titulo': 'Teste', 'descricao': f'{self.uuid.int}', 'url': 'http://blank.page'}

        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Video.objects.filter(descricao__iexact=f'{self.uuid.int}').count(), 1)
        self.assertEqual(self.response.data, expected_response)


    def test_if_any_data_is_blank_dont_create_a_video_and_return_400(self):
        """
        (ERROR) Se algum dado estiver vazio não crie um video e retorne 400.
        """
        """
            *url
            *uuid
            *data
            !response
        """
        self.data["url"] = ""
        
        expected_response = {"url":["Url está em branco, por favor preencha corretamente."]}
        response = self.client.post(self.url, self.data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, expected_response)
        
    def test_when_changing_value_return_a_json_with_values_and_200(self):
        """
        (PUT) Quando trocando um dado, retorne um json com os dados e 200.
        """
        """
            *url
            *uuid
            *data
            *response
        """
        data2 = {
            "titulo": "Teste2",
            "descricao": f"{self.uuid.hex}",
            "url": "http://blank.page"
        }

        expected_response = {"id":1,"titulo":"Teste2","descricao":f"{self.uuid.hex}","url":"http://blank.page"}
        response = self.client.put('/videos/1/',data2, format='json', follow=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_response)

    

"""
    * = DONE
    ! = TODO
    ? = What are beeing tested
    // = depreciated
    
    TODO:
    ?CRUD
    *post
    *put
    !delete
    !get-all
    !get-one
    
    ?ERRORS (exceptions)
    *blank
    !max_length
    !invalid
"""

"""
data2 = {
            "titulo": "Teste2",
            "descricao": f"{self.uuid.hex}",
            "url": "http://blank.page"
        }
success delete:
    {"detail": "Vídeo deletado com sucesso!"}
dont find delete:
    {"detail": "Vídeo não encontrado."}
"""
