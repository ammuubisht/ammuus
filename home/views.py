from django.shortcuts import render
from .models import Project

# Create your views here.
def homepage(request):
    projects = Project.objects.all()
    context = {'projects':projects}
    return render(request, 'home/homepage.html', context)

def aboutme(request):
    return render(request, 'home/about-me.html')

def projects(request):
    projects = Project.objects.all()
    context = {'projects':projects}
    return render(request, 'home/projects.html', context)

def contactMe(request):
    return render(request, 'home/contact-me.html')

def Resume(request):
    return render(request, 'home/resume.html')
