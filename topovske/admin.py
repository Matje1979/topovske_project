from django.contrib import admin

# Register your models here.

from .models import Index, Project, Current, PublicCampaign, CampHistory, Camp, Archive, Victim, Photo, Interview, Location

admin.site.register(Index)
admin.site.register(Project)
admin.site.register(Current)
admin.site.register(PublicCampaign)
admin.site.register(CampHistory)
admin.site.register(Camp)
admin.site.register(Archive)
admin.site.register(Location)
admin.site.register(Victim)
admin.site.register(Photo)
admin.site.register(Interview)
