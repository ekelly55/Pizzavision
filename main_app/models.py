
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

class Character(models.Model):
    name = models.CharField(max_length=150)
    actor = models.CharField(max_length=150)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE, related_name='characters')

    def __str__(self):
        return self.name

class PizzaClub(models.Model):
    club_name = models.CharField(max_length=150)
    characters = models.ManyToManyField(Character)
    def __str__(self):
        return self.club_name
