from django.db import models
from hadeethapp.constants import HADEETH_BOOKS

class HadeethBook(models.Model):
    book_name =
    author =
    tasneef =

class TasneefRawy(models.Model):
    mosannef =
    rawy_adala_factor =
    rawy_dabt_factor =
    rawy_theqa_factor =

class Sanad(models.Model):
    rawy_name =
    rawy_knowledge_way =   # 3n or same3a or what?


class Rawy(models.Model):
    rawy_name =
    rawy_birth_date =
    rawy_death_date =
    rawy_tasneef = models.ForeignKey(TasneefRawy)

class Hadeeth(models.Model):
    full_hadeeth =
    matn =
    sanad =
    book =
    sanad =
    shozoz =
    ella =
    tasneef =

class HadeethStrength(models.Model):
    sanad_strength =
    hadeeth_strength =
