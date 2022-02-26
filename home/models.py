from django.db import models


# Create your models here.
class Project(models.Model):
    project_name = models.CharField(max_length=255)
    project_tagline = models.CharField(max_length=255)
    thumbnail = models.ImageField()
    project_url = models.CharField(max_length=255)

    def __str__(self):
        return self.project_name

