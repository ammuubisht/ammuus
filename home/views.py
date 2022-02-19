from django.shortcuts import render

# Create your views here.
def homepage(request):
    context = {}
    return render(request, 'home/homepage.html', context)

def aboutme(request):
    return render(request, 'home/about-me.html')

def projects(request):
    # project = Project.objects.all()
    context = {}
    return render(request, 'home/projects.html', context)

def contactMe(request):
    return render(request, 'home/contact-me.html')

def Resume(request):
    return render(request, 'home/resume.html')
