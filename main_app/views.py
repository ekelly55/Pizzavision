from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Character, Pizza
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView


# Create your views here.

class Home(TemplateView):
    template_name = 'home.html'

class About(TemplateView):
    template_name = 'about.html'

class PizzaList(TemplateView):
    template_name = 'pizza_list.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context['pizzas'] = Pizza.objects.filter(name__icontains=name)
            context['header'] = f"Searching for {name}"
        else:
            context['pizzas'] = Pizza.objects.all()
            context['header'] = "Check out this za!"
        return context


class PizzaCreate(CreateView):
    model = Pizza
    fields = ['image', 'name', 'review']
    template_name = 'pizza_create.html'
    success_url = '/pizzas/'

class PizzaUpdate(UpdateView):
    model = Pizza
    fields = ['image', 'name', 'review']
    template_name = 'pizza_update.html'
    def get_success_url(self):
        return reverse('pizza_detail', kwargs= {'pk': self.object.pk})

class PizzaDetail(DetailView):
    model = Pizza
    template_name = 'pizza_detail.html'

class PizzaDelete(DeleteView):
    model = Pizza
    template_name = 'pizza_delete_confirmation.html'
    success_url = '/pizzas/'

class CharacterCreate(View):
    def post(self, request, pk):
        name = request.POST.get('name')
        actor = request.POST.get('actor')
        pizza = Pizza.objects.get(pk=pk)
        Character.objects.create(name=name, actor=actor, pizza=pizza)
        return redirect('pizza_detail', pk=pk)