from django.contrib import admin
from contato import models


@admin.register(models.Categoria)
class Categoria(admin.ModelAdmin):
    list_display = "nome"


@admin.register(models.Contato)
class Contato(admin.ModelAdmin):
    list_display = "nome", "sobrenome", "telefone"
    list_per_page = 10
    list_max_show_all = 200
