from django.contrib import admin

# Register your models here.

from .models import Index, Project, Camp, Archive, Victim, Photo, Interview

admin.site.register(Index)
admin.site.register(Project)
admin.site.register(Camp)
admin.site.register(Archive)
admin.site.register(Victim)
admin.site.register(Photo)
admin.site.register(Interview)
