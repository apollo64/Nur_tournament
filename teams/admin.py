from django.contrib import admin
from teams.models import Team, Division, Game

# import models import Team# Register your models here.

admin.site.register(Team)
admin.site.register(Division)
admin.site.register(Game)

