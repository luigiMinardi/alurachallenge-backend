from django.contrib import admin
from obeflix_back.models import Video


class Videos(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'descricao', 'url')
    list_display_links = ('id', 'titulo')
    search_fields = ('titulo', 'url',)
    list_per_page = 20

admin.site.register(Video, Videos)