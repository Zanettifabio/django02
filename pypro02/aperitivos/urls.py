from django.urls import path
from pypro02.aperitivos.views import video


app_name = 'aperitivos'
urlpatterns = [
    path('<slug:slug>', video, name='video')
]