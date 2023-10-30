from django.db import models
from django.utils import timezone


class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self)->str:
        return f"{self.nome}"


class Contato(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50, blank=True)
    telefone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True)
    criado = models.DateTimeField(default=timezone.now)
    desc = models.TextField(blank=True)
    mostrar = models.BooleanField(default=False)
    imagem = models.ImageField(blank=True, upload_to="imagens/%Y/%m/")
    categoria = models.ForeignKey(
        Categoria, 
        on_delete=models.SET_NULL, 
        blank=True, 
        null=True
    )

    def __str__(self) -> str:
        return f"{self.nome} {self.sobrenome}"
