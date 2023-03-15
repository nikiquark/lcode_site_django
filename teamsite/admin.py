from django.contrib import admin

# Register your models here.

from .models import Person, Publication

admin.site.register(Person)
admin.site.register(Publication)
