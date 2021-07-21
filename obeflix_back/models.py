from django.db import models
from django.core.validators import URLValidator, MaxLengthValidator


class Video(models.Model):
    titulo = models.CharField(
        max_length=30,
        help_text="Coloque o título do vídeo",
    )
    descricao = models.CharField(
        max_length=300,
        help_text="Coloque a descrição do vídeo",
    )
    url = models.URLField(
        max_length=200,
        help_text="Coloque o link para o vídeo",
    )

    def __str__(self):
        return self.titulo
