from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Index, Project, Victim, Photo, Location, CampHistory, Current, PublicCampaign, Interview, Archive, Video, Support
from django.http import JsonResponse
from django.forms.models import model_to_dict
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models.fields.files import ImageFieldFile

# Create your views here.


def home(request):
    location = "naslovna"
    indexes = Index.objects.all()
    context = {"location": location, "indexes": indexes}
    return render(request, 'topovske/index.html', context)


def project(request):
    projects = Project.objects.all()
    support = Support.objects.all()
    print (projects)
    location = "projekat"
    if len(projects) > 0:
        context = {"projects": projects[0], "support": support[0], "location": location}
    else:
        context = {"location": location}
    return render(request, 'topovske/o_projektu.html', context)


def logor(request):
    camp_history = CampHistory.objects.all()
    
    current = Current.objects.all()
    
    public_campaign = PublicCampaign.objects.all()
    
    location = "logor"
    try:
        context = {"camp_history": camp_history[0], "current": current[0], "public_campaign": public_campaign[0], "location": location}    

    except IndexError:
        
        context = {"location": location}
    
    return render(request, 'topovske/o_logoru.html', context)
        


def map(request):
    locations = Location.objects.all()
    location = "mapa"
    context = {"location": location, "locations": locations}
    return render(request, 'topovske/mapa.html', context)


def foto(request):
    photos = Photo.objects.all()
    paginator = Paginator(photos, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    location = "foto"

    count = 0
    p_slides = []
    slide = []
    num = 0
    while num < len(photos):
        slide = []
        for i in range(count, count + 12):
            try:
                slide.append(photos[i])
                num += 1
            except IndexError:
                break 

        count += 12
        p_slides.append(slide)


    context = {"location": location, "p_slides": p_slides, "page_obj": page_obj}
    return render(request, 'topovske/foto.html', context)


def archive(request):

    url = request.path
    if 'en' in url:
        url = url[3:]
    else:
        url = url

    letters = Archive.objects.filter(category = '0')
    
    count = 0
    l_slides = []
    slide = []
    num = 0
    while num < len(letters):
        slide = []
        for i in range(count, count + 5):
            try:
                slide.append(letters[i])
                num += 1
            except IndexError:
                break 

        count += 5
        l_slides.append(slide) 

    location = "arhiva"
    context = {"location": location, "l_slides": l_slides, "url": url}
    return render(request, 'topovske/arhiva.html', context)

def docs(request):
    url = request.path
    if 'en' in url:
        url = url[3:]
    else:
        url = url

    documents = Archive.objects.filter(category = '3')

    count = 0
    d_slides = []
    slide = []
    num = 0
    while num < len(documents):
        slide = []
        for i in range(count, count + 5):
            try:
                slide.append(documents[i])
                num += 1
            except IndexError:
                break 

        count += 5
        d_slides.append(slide)

    context = {"d_slides": d_slides, "url": url}

    return render(request, 'topovske/dokumenti.html', context)

def victim_list(request):
    url = request.path
    if 'en' in url:
        url = url[3:]
    else:
        url = url   

    victims_list = Archive.objects.filter(category = '1')
    count = 0
    v_slides = []
    slide = []
    num = 0
    while num < len(victims_list):
        slide = []
        for i in range(count, count + 5):
            try:
                slide.append(victims_list[i])
                num += 1
            except IndexError:
                break 

        count += 5
        v_slides.append(slide)

    context = {"v_slides": v_slides, "url": url}

    return render(request, 'topovske/spisak.html', context)

def testimonies(request):
    url = request.path
    if 'en' in url:
        url = url[3:]
    else:
        url = url
    testimonies = Archive.objects.filter(category = '2')
    count = 0
    t_slides = []
    slide = []
    num = 0
    while num < len(testimonies):
        slide = []
        for i in range(count, count + 5):
            try:
                slide.append(testimonies[i])
                num += 1
            except IndexError:
                break 

        count += 5
        t_slides.append(slide)

    context = {"t_slides": t_slides, "url": url}
    return render(request, 'topovske/svedocenja.html', context)

def photos(request):
    url = request.path
    if 'en' in url:
        url = url[3:]
    else:
        url = url
    photos = Archive.objects.filter(category = '4')

    count = 0
    p_slides = []
    slide = []
    num = 0
    while num < len(photos):
        slide = []
        for i in range(count, count + 5):
            try:
                slide.append(photos[i])
                num += 1
            except IndexError:
                break 

        count += 5
        p_slides.append(slide)
    context = {"p_slides": p_slides, "url": url}
    return render(request, 'topovske/fotografije.html', context)


def getItems(request, categ):

    items = Archive.objects.filter(category = categ)

        # print (item.image.path)
    new_list = []
    for item in items:
        new_list.append(model_to_dict(item))

    for item in new_list:
        item['image'] = items.get(id=item['id']).image.path

    print ('New_list: ', new_list)
    
    return JsonResponse({'new_list': new_list}, safe = False)


def dbase(request):
   
    if 'surname' in request.GET:
        victims = Victim.objects.filter(surname=request.GET.get('surname'))
    elif 'nationality' in request.GET:
        victims = Victim.objects.filter(nationality=request.GET.get('nationality'))
    else:
        victims = Victim.objects.all()

    count = 0
    db_slides = []
    slide = []
    num = 0
    while num < len(victims):
        slide = []
        for i in range(count, count + 20):
            try:
                slide.append(victims[i])
                num += 1
            except IndexError:
                break 

        count += 20
        db_slides.append(slide)

    location = "baza_podataka"
    context = {"victims": victims, "db_slides": db_slides, "location": location}
    return render(request, 'topovske/baza.html', context)


def video(request):

    url = request.path
    if 'en' in url:
        url = url[3:]
    else:
        url = url

    videos = Video.objects.all().order_by('date')

    count = 0
    vid_slides = []
    slide = []
    num = 0
    while num < len(videos):
        slide = []
        for i in range(count, count + 12):
            try:
                slide.append(videos[i])
                num += 1
            except IndexError:
                break 

        count += 12
        vid_slides.append(slide)

    location = "video"
    context = {"location": location, "vid_slides": vid_slides, "url": url}
    return render(request, 'topovske/video.html', context)

def intervju(request):

    interviews = Interview.objects.all()
    context = {'interviews': interviews}
    return render(request, 'topovske/interviews.html', context)

# def singlePhoto(request, info):
    
#     foto_object = Archive.objects.get(id=info)
#     return render(request, 'topovske/single-foto.html', context)