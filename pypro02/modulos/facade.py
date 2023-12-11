from typing import List
from pypro02.modulos.models import Modulo


def listar_modulos_ordenados() -> List[Modulo]:  # Anotation que indica que o retorno será uma lista e cada objeto desta
    # lista será um Módulo.
    """
    Lista os módulos ordenando pelo título.
    :return: Lista dos módulos ordenados pelo título.
    """
    return list(Modulo.objects.order_by('order').all())


def encontrar_modulo(slug) -> Modulo:
    return Modulo.objects.get(slug=slug)


def listar_aulas_de_modulo_ordenadas(modulo):
    return list(modulo.aula_set.order_by('order').all())
