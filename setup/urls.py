from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from obeflix_back.views import CategoriasViewSet, VideosViewSet, ListaVideosPorCategoria, ListaVideosFree

router = routers.DefaultRouter()
router.register('videos', VideosViewSet, basename='Videos')
router.register('categorias', CategoriasViewSet, basename='Categorias')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('videos/free/', ListaVideosFree.as_view()),
    path('categorias/<int:pk>/videos/', ListaVideosPorCategoria.as_view()),
    path('', include(router.urls))
]
