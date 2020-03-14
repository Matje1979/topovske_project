from django.shortcuts import render
from .models import Index, Project

# Create your views here.


def home(request):
    location = "naslovna"
    indexes = Index.objects.all()
    context = {"location": location, "indexes": indexes}
    return render(request, 'topovske/index.html', context)


def project(request):
    projects = Project.objects.all()
    location = "projekat"
    context = {"projects": projects, "location": location}
    return render(request, 'topovske/o_projektu.html', context)


def logor(request):

    url = request.path
    if 'en' in url:
        url = url[3:]
    else:
        url = url

    location = "logor"
    context = {"location": location, "url": url}
    return render(request, 'topovske/o_logoru.html', context)


def map(request):

    url = request.path
    if 'en' in url:
        url = url[3:]
    else:
        url = url

    location = "mapa"
    context = {"location": location, "url": url }
    return render(request, 'topovske/mapa.html', context)


def foto(request):

    url = request.path
    if 'en' in url:
        url = url[3:]
    else:
        url = url

    location = "foto"
    context = {"location": location, "url": url}
    return render(request, 'topovske/foto.html', context)


def archive(request):

    url = request.path
    if 'en' in url:
        url = url[3:]
    else:
        url = url

    location = "arhiva"
    context = {"location": location, "url": url}
    return render(request, 'topovske/arhiva.html', context)


def dbase(request):

    url = request.path
    if 'en' in url:
        url = url[3:]
    else:
        url = url

    location = "baza_podataka"
    context = {"location": location, "url": url}
    return render(request, 'topovske/baza.html', context)


def video(request):

    url = request.path
    if 'en' in url:
        url = url[3:]
    else:
        url = url

    location = "video"
    context = {"location": location, "url": url}
    return render(request, 'topovske/video.html', context)