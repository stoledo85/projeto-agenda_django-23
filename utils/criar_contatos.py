import os
import sys
from datetime import datetime
from pathlib import Path
from random import choice

import django 
from django.conf import settings

DJANGO_BASE_DIR = Path(__file__).parent.parent
NUMBER_OF_OBJECTS = 1000

sys.path.append(str(DJANGO_BASE_DIR))
os.environ["DJANGO_SETTINGS_MODULE"] = "project.settings"
settings.USE_TZ = False

django.setup()

if __name__ == "__main__":
    import faker
    from contato.models import Categoria, Contato

    Contato.objects.all().delete()
    Categoria.objects.all().delete()

    fake = faker.Faker("pt_BR")
    categoria = ["Amigos", "Família", "Conhecidos"]
    django_categorias = [Categoria(nome=nome) for nome in categoria]
    for categoria in django_categorias:
        categoria.save()

    django_contatos = []
    for _ in range(NUMBER_OF_OBJECTS):
        profile = fake.profile()
        email = profile["mail"]
        first_name, last_name = profile["name"].split(" ", 1)
        phone = fake.phone_number()
        created_date: datetime = fake.date_this_year()
        description = fake.text(max_nb_chars=100)
        category = choice(django_categorias)
        django_contatos.append(
            Contato(
                nome=first_name,
                sobrenome=last_name,
                telefone=phone,
                email=email,
                criado=created_date,
                desc=description,
                categoria=category,
            )
        )
    if len(django_contatos) > 0:
        Contato.objects.bulk_create(django_contatos)
