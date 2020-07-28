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
    path('arhiva/', views.archive, name="topovske-arhiva"),
    path('arhiva/spisak', views.victim_list, name="topovske-spisak"),
    path('arhiva/dokumenti', views.docs, name="topovske-dokumenti"),
    path('arhiva/svedocenja', views.testimonies, name="topovske-svedocenja"),
    path('arhiva/fotografije', views.photos, name="topovske-fotografije"),
    path('baza_podataka/', views.dbase, name="topovske-baza-podataka"),
    path('foto/', views.foto, name="topovske-foto"),
    path('video/', views.video, name="topovske-video"),
    path('intervju/', views.intervju, name="topovske-intervju"),
    path('<str:categ>/', views.getItems, name="get-archive-items"),
    # path('/', views.getItems, name="get-archive-items"),
    url(r'^i18n/', include('django.conf.urls.i18n')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
