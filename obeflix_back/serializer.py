from rest_framework import serializers
from obeflix_back.models import Video, Categoria


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class ListaVideoPorCategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'

class ListaVideoFreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'