from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Index, Project, Victim, Photo, Location, CampHistory, Current, PublicCampaign

# Create your views here.


def home(request):
    location = "naslovna"
    indexes = Index.objects.all()
    context = {"location": location, "indexes": indexes}
    return render(request, 'topovske/index.html', context)


def project(request):
    projects = Project.objects.all()
    location = "projekat"
    context = {"projects": projects[0], "location": location}
    return render(request, 'topovske/o_projektu.html', context)


def logor(request):
    camp_history = CampHistory.objects.all()
    current = Current.objects.all()
    public_campaign = PublicCampaign.objects.all()
    location = "logor"
    context = {"camp_history": camp_history[0], "current": current[0], "public_campaign": public_campaign[0], "location": location}
    return render(request, 'topovske/o_logoru.html', context)


def map(request):
    locations = Location.objects.all()
    location = "mapa"
    context = {"location": location, "locations": locations}
    return render(request, 'topovske/mapa.html', context)


def foto(request):
    photos = Photo.objects.all()
    paginator = Paginator(photos, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    location = "foto"
    context = {"location": location, "page_obj": page_obj}
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
    victims = Victim.objects.all()
    if 'surname' in request.GET:
        victims = victims.filter(surname=request.GET.get('surname'))
    if 'nationality' in request.GET:
        victims = victims.filter(nationality=request.GET.get('nationality'))
    location = "baza_podataka"
    context = {"victims": victims, "location": location}
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