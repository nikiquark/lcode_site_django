from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

from .models import Person, Publication

# Create your views here.

def index(request):
    context = {
        'title': 'About',
    }
    return render(request, "teamsite/index.html", context)

def partnership(request):
    context = {
        'title' : 'Partnership'
    }
    return render(request, "teamsite/partnership.html", context)

def team(request):
    
    context = {
        'title' : 'Team',
        'persons': Person.objects.all()
    }
    return render(request, "teamsite/team.html", context)

def publications(request):
    def prepare_publications():
        publications = Publication.objects.all()
        years = sorted(set([i.year for i in publications]), reverse=True)
        result = {year: [pub for pub in publications if pub.year == year] for year in years}
        # print(result)
        return result

    context = {
        'title' : 'LC | Team',
        'publications': prepare_publications()
    }
    return render(request, "teamsite/publications.html", context)
