from django.shortcuts import render
from contato.models import Contato


def index(request):
    contato = Contato.objects.filter(mostrar=True)
    contexto = {
        "contatos": contato,
    }
    return render(request, "contato/index.html", contexto)
