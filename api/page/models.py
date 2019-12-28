from django.db import models
from django.utils import timezone

class Processor(models.Model):
    Title = models.CharField(max_length=50)
    Model = models.CharField(max_length=50)
    Series = models.CharField(max_length=50, default = None)
    Company = models.CharField(max_length=50)
    Frequency = models.FloatField(default=0)
    Chache_Memory = models.IntegerField(default=0)
    Cores = models.IntegerField(default=0)
    Socket = models.CharField(max_length=50)
    Graphics_Core = models.BooleanField(default=False)
    Price = models.FloatField(default=0)
    Add_Date = models.DateTimeField(default = timezone.now())

    def __str__(self):
        return "{} {} {} - {}".format(self.Company, self.Model, self.Series, self.Add_date)