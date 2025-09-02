from django.contrib import admin
from .models import Alimento

@admin.register(Alimento)
class AlimentoAdmin(admin.ModelAdmin):
	list_display = ("nome", "peso", "quantidade", "preco_por_unidade")
