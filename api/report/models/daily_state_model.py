from django.db import models


class DailyState(models.Model):

    BROADCASTS=[(0, 'false'),(1, 'true')]

    datasource = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    suspects = models.PositiveSmallIntegerField(default=0)
    refuses = models.PositiveSmallIntegerField(default=0)
    cases = models.PositiveSmallIntegerField(default=0)
    casesNew = models.PositiveSmallIntegerField(default=0)
    deaths = models.PositiveSmallIntegerField(default=0)
    deathsNew = models.PositiveSmallIntegerField(default=0)
    broadcasts = models.PositiveSmallIntegerField(choices=BROADCASTS)
    comments = models.TextField()


