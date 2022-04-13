from pyexpat import model
from django.db import models

# Create your models here.
class Subscriber(models.Model):
    email = models.EmailField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class Project(models.Model):
    title = models.CharField(max_length=100, unique=True)
    team = models.CharField(max_length=100)
    description = models.TextField()
    rating = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.title
