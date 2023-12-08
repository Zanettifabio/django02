# from django.shortcuts import render
from django.http import HttpResponse


def detalhe(request, slug):
    return HttpResponse('Detalhe do módulo')
