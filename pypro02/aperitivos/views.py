from django.shortcuts import render


def video(request, slug):
    video = {"titulo": "Vídeo Aperitivo: Amostra", "vimeo_id": 887979526}
    return render(request, 'aperitivos/video.html', context={"video": video})
