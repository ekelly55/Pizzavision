from django.contrib import admin
from .models import Character, Pizza, PizzaClub

admin.site.register(Pizza)
admin.site.register(Character)
admin.site.register(PizzaClub)

# Register your models here.
