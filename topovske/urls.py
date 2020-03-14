from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls import include, url, re_path
from . import views
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name="topovske-naslovna"),
    path('projekat/', views.project, name="topovske-projekat"),
    path('o_logoru/', views.logor, name="topovske-o-logoru"),
    path('mapa/', views.map, name="topovske-mapa"),
    path('arhiva/', views.archive, name="topovske-arhiva"),
    path('baza_podataka/', views.dbase, name="topovske-baza-podataka"),
    path('foto/', views.foto, name="topovske-foto"),
    path('video/', views.video, name="topovske-video"),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
