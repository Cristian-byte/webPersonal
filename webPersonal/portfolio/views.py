from django.shortcuts import render
from .models import Project

# Create your views here.

def portfolio(request):
    projects = Project.objects.all()  
    return render(request, "portfolio/portfolio.html", 
        {'projects':projects})


def portfolio(request):
    return render(request, "core/portfolio.html")
