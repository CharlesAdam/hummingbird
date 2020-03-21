from django.db import models


class DailyBrasilIO(models.Model):

    PLACE_TYPE=[('city', 'cidade'),('state', 'estado')]

    city = models.CharField(max_length=255)
    cases = models.PositiveSmallIntegerField(default=0)
    date = models.DateField()
    deaths = models.PositiveSmallIntegerField(default=0)
    discarded = models.PositiveSmallIntegerField(default=0)
    notes = models.TextField()
    notified = models.PositiveSmallIntegerField(default=0)
    place_type = models.CharField(choices=PLACE_TYPE)
    source_url = models.TextField()
    state = models.CharField(max_length=2)
    suspect = models.PositiveSmallIntegerField(default=0)



