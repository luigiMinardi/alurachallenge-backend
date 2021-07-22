from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

from obeflix_back.models import Video

class VideoTestCase(APITestCase):

    def setUp(self):
        self.url = reverse('Videos-list')
        self.data = {
            "titulo":"Teste",
            "descricao":"Isso é um teste",
            "url":"http://blank.page"
        }
        self.data2 = {
            "titulo":"Teste2",
            "descricao":"Isso é um teste2",
            "url":"http://blank.page"
        }

    def test_create_video(self):
        """
        Certifica que podemos criar um video.
        """
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Video.objects.count(), 1)
        self.assertEqual(Video.objects.get().titulo, 'Teste')

