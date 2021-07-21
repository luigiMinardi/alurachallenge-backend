from rest_framework import viewsets, status
from rest_framework.response import Response
from obeflix_back.models import Video
from obeflix_back.serializer import VideoSerializer


class VideosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os vídeos"""
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

    def destroy(self, request, *args, **kwargs):
        """Deletando um video"""
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"detail": "Vídeo não encontrado."})
        return Response(status=status.HTTP_200_OK, data={"detail": "Vídeo deletado com sucesso!"})
