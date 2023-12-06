from django.db import models
from django.urls import reverse

# Create your models here.
class Friend(models.Model):
    name = models.CharField(max_length=20)
    breed = models.CharField(max_length=50)
    age = models.IntegerField()
    habitat = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'friend_id': self.id})