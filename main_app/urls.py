from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='Home'),
    path('about/', views.About.as_view(), name='About'),
    path('pizzas/', views.PizzaList.as_view(), name = 'pizzas'),
    path('pizzas/new/', views.PizzaCreate.as_view(), name='pizza_create'),
    path('pizzas/<int:pk>/', views.PizzaDetail.as_view(), name='pizza_detail'),
    path('pizzas/<int:pk>/update', views.PizzaUpdate.as_view(), name='pizza_update'),
    path('pizzas/<int:pk>/delete', views.PizzaDelete.as_view(), name='pizza_delete'),
    path('pizzas/<int:pk>/characters/new/', views.CharacterCreate.as_view(), name='character_create'),
    path('pizzaclubs/<int:pk>/characters/<int:character_pk>/', views.PizzaclubCharacterAssoc.as_view(), name='pizzaclub_character_assoc'),
] 