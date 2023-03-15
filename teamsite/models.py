import datetime
from django.db import models

# Create your models here.

class Person(models.Model):
    full_name = models.CharField(max_length=256)
    post =  models.CharField(max_length=256)
    email = models.EmailField()
    bio = models.TextField(blank=True)
    picture = models.ImageField(upload_to='pictures',
                                default='/pictures/circleempty.png')

    def __str__(self):
        return self.full_name

    def __unicode__(self):
        return self.__str__()

class Publication(models.Model):
    title = models.CharField(max_length=256)
    description = models.CharField(max_length=400)
    url = models.CharField(max_length=400)
    year = models.IntegerField(choices=[(r,r) for r in range(1995, datetime.date.today().year+2)])

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.__str__()