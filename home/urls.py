from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('about-me/', views.aboutme, name="about-me"),
    path('projects/', views.projects, name="projects"),
    path('contact-me/', views.contactMe, name="contact-me")

]