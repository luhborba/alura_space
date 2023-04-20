from django.contrib import admin
from .models import Fotografia

# Register your models here.
class FotografiaAdmin(admin.ModelAdmin):
    list_display = ('id','nome','legenda','foto','categoria','publicado')
    list_display_links = ('id','nome')
    list_editable = ('publicado',)
    search_fields = ('id','nome','legenda','descricao')
    list_filter = ('categoria','publicado')
    list_per_page = 10
    ordering = ('id',)


admin.site.register(Fotografia, FotografiaAdmin)