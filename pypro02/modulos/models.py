from django.db import models
from ordered_model.models import OrderedModel


class Modulo(OrderedModel):
    titulo = models.CharField(max_length=64)
    publico = models.TextField()
    descricao = models.TextField()

    def __str__(self):
        return self.titulo
