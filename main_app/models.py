
from django.db import models

# Create your models here.

class Pizza(models.Model):
    image = models.CharField(max_length=250)
    name = models.CharField(max_length=100)
    review = models.TextField(max_length=500)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']
