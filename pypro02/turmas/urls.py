from django.urls import path
from pypro02.turmas import views


app_name = 'turmas'
urlpatterns = [
    path('', views.indice, name='indice')
]
