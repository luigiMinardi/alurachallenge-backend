from rest_framework import viewsets, status, filters, generics
from rest_framework.response import Response

from obeflix_back.models import Video, Categoria
from obeflix_back.serializer import VideoSerializer, CategoriaSerializer, ListaVideoPorCategoriaSerializer


class VideosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os vídeos"""
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    # "search" query param
    filter_backends = [filters.SearchFilter]
    search_fields = ['titulo']

    def destroy(self, request, *args, **kwargs):
        """(DELETE) Deletando um video"""
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND, data={'detail': 'Vídeo não encontrado.'})
        return Response(status=status.HTTP_200_OK, data={'detail': 'Vídeo deletado com sucesso!'})

class CategoriasViewSet(viewsets.ModelViewSet):
    """Exibindo todas as categorias"""
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

    def destroy(self, request, *args, **kwargs):
        """(DELETE) Deletando uma categoria"""
        try:
            instance = self.get_object()
            if instance == Categoria.objects.get(id__iexact=1):
                return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED , data={'detail': 'Você não pode deletar a categoria 1.'})
            else:
                self.perform_destroy(instance)
        except: 
            return Response(status=status.HTTP_404_NOT_FOUND, data={'detail': 'Categoria não encontrada.'})
        return Response(status=status.HTTP_200_OK, data={'detail': 'Categoria deletada com sucesso!'})

class ListaVideosPorCategoria(generics.ListAPIView):
    """Lista os videos em uma Categoria"""
    def get_queryset(self):
        queryset = Video.objects.filter(categoriaId=self.kwargs['pk'])
        return queryset
    
    serializer_class = ListaVideoPorCategoriaSerializer

    # "search" query param
    filter_backends = [filters.SearchFilter]
    search_fields = ['titulo']
