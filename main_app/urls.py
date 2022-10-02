from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='Home'),
    path('about/', views.About.as_view(), name='About'),
    path('pizzas/', views.PizzaList.as_view(), name = 'pizzas'),
]