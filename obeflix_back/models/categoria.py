from django.db import models
from django.core.validators import RegexValidator

class Categoria(models.Model):
    titulo = models.CharField(
        max_length=30,
        help_text="Coloque o título da categoria"
    )
    cor = models.CharField(
        max_length=7,
        help_text="Coloque a cor em hexadecimal",
        validators=[RegexValidator(r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$')]
    )

    def __str__(self):
        return self.titulo