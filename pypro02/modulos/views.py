from django.shortcuts import render
from pypro02.modulos import facade


def detalhe(request, slug):
    modulo = facade.encontrar_modulo(slug)
    aulas = facade.listar_aulas_de_modulo_ordenadas(modulo)
    return render(request, 'modulos/modulo_detalhe.html', context={'modulo': modulo, 'aulas': aulas})
