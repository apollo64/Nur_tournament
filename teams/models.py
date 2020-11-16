from django.db import models


# Create your models here.

class Team(models.Model):
    name = models.CharField(max_length=120, null=False, blank=False, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField(default=0)


class Division(models.Model):
    name = models.CharField(max_length=10)
    name_teams = models.ForeignKey(Team,
                                   on_delete=models.PROTECT,
                                   related_name='division_name_teams',null=True, blank=True)


class Game(models.Model):
    team_1 = models.ForeignKey(Team,
                               on_delete=models.PROTECT,
                               related_name='team_1')
    team_2 = models.ForeignKey(Team,
                               on_delete=models.PROTECT,
                               related_name='team_2')
    result_1 = models.IntegerField(default=0)
    result_2 = models.IntegerField(default=0)
    division = models.ForeignKey(Division,
                                 on_delete=models.PROTECT,
                                 related_name='division')


