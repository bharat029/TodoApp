from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Schedule(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length = 50)
    description = models.CharField(max_length = 500)
    deadline = models.DateTimeField()
    
    def get_absolute_url(self):
        return reverse('schedule:index')
    
    def __str__(self):
        return self.title
    