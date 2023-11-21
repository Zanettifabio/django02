# from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('<html><meta charset="UTF-8" /><body>Olá, Django</body></html>',
                        content_type='text/html')
