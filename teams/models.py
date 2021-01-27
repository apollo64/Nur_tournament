from django.db import models


# Create your models here.

class Division(models.Model):
    name = models.CharField(max_length=10, blank=True, null=True)


class Team(models.Model):
    name = models.CharField(max_length=120, null=False, blank=False, unique=True)
    created_date = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField(default=0)
    division = models.ForeignKey(Division, related_name='division_of_team', null=True, on_delete=models.PROTECT)

    def __str__(self):
        """String for representing the Team object (in Admin site etc.)."""
        return self.name


class Game(models.Model):
    winner = models.ForeignKey(Team,
                               on_delete=models.PROTECT,
                               related_name='team_win', default=None)
    loser = models.ForeignKey(Team,
                              on_delete=models.PROTECT,
                              related_name='team_los', default=None)
    round = models.IntegerField(default=0)
