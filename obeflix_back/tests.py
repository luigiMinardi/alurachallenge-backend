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


    def test_if_data_is_valid_return_the_created_video_and_201(self):
        """
        (POST) Se os dados são válidos, retorne o video criado em um json e 201.
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

    def test_when_deleting_video_return_a_json_of_success_and_200(self):
        """
        (DELETE) Quando deletando um video retorne um json de sucesso e 200.
        """
        """
            *url
            *uuid
            *data
            *response
        """
        expected_response = {"detail": "Vídeo deletado com sucesso!"}
        response = self.client.delete('/videos/1/', follow=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_response)
    
    def test_when_getting_a_video_return_a_json_with_the_video_and_200(self):
        """
        (GET) Quando prucurando um video retorne um json com o video e 200.
        """
        """
            *url
            *uuid
            *data
            *response
        """

        expected_response = {"id":1,"titulo":"Teste","descricao":f"{self.uuid.int}","url":"http://blank.page"}
        response = self.client.get("/videos/1/")
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_response)

    def test_when_getting_all_videos_return_a_json_with_all_videos_and_200(self):
        """
        (GET) Quando procurando todos os videos retorne um json com todos os videos e 200.
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
        self.client.post(self.url, data2, format='json')

        expected_response = [
            OrderedDict([('id', 1), ('titulo', 'Teste'), ('descricao', f'{self.uuid.int}'), ('url', 'http://blank.page')]), 
            OrderedDict([('id', 2), ('titulo', 'Teste2'), ('descricao', f'{self.uuid.hex}'), ('url', 'http://blank.page')])
        ]
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_response)

    def test_if_any_data_is_blank_return_return_a_custom_blank_json_error_and_400(self):
            """
            (ERROR-BLANK) Se algum dado estiver vazio retorne um json com o erro de onde estiver vazio e 400.
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

    def test_if_any_data_has_more_length_than_the_max_return_a_custom_length_json_error_and_400(self):
        """
        (ERROR-MAX_LENGTH) Se algum dado exceder o tamanho retorne um json com o erro de tamanho e 400.
        """
        """
            *url
            *uuid
            *data
            !response
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
            !response
        """
        self.data["url"] = "blank.page"

        expected_response = {'url': ['Url inválida!']}
        response = self.client.post(self.url, self.data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, expected_response)
    

        """
            ?url
            ?uuid
            ?data
            ?response
        """
"""
    * = DONE
    ! = TODO
    ? = What are beeing tested
    // = type
    
    TODO:
    ?CRUD
    *post
    *put
    *delete
    *get-all
    *get-one
    
    ?ERRORS (exceptions)
    // post
    *blank
    *max_length
    *invalid
    //put
    !put-video-inexistente
    !put-with-exception
    //delete
    !delete-video-inexistente
    //get
    !get-video-inexistente
    !get-blank-data-base

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
