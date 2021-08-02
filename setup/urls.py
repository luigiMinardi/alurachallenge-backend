from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from obeflix_back.views import CategoriasViewSet, VideosViewSet

router = routers.DefaultRouter()
router.register('videos', VideosViewSet, basename='Videos')
router.register('categorias', CategoriasViewSet, basename='Categorias')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
