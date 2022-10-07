from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Character, Pizza, Pizzaclub
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.
@method_decorator(login_required, name = 'dispatch')
class Home(TemplateView):
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #if Pizzaclub.objects.user != None:
        context['pizzaclubs'] = Pizzaclub.objects.filter(user = self.request.user)
        #context['pizzaclubs'] = Pizzaclub.objects.all()
        #else:
            #context = "Make some Pizza Clubs"
        return context

class About(TemplateView):
    template_name = 'about.html'

@method_decorator(login_required, name = 'dispatch')
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

@method_decorator(login_required, name = 'dispatch')
class PizzaCreate(CreateView):
    model = Pizza
    fields = ['image', 'name', 'review']
    template_name = 'pizza_create.html'
    success_url = '/pizzas/'

@method_decorator(login_required, name = 'dispatch')
class PizzaclubCreate(CreateView):
    model = Pizzaclub
    fields = ['club_name', 'characters', 'user']
    template_name = 'pizzaclub_create.html'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PizzaclubCreate, self).form_valid(form)

    success_url = '/'

@method_decorator(login_required, name = 'dispatch')
class PizzaUpdate(UpdateView):
    model = Pizza
    fields = ['image', 'name', 'review']
    template_name = 'pizza_update.html'
    def get_success_url(self):
        return reverse('pizza_detail', kwargs= {'pk': self.object.pk})

@method_decorator(login_required, name = 'dispatch')
class PizzaDetail(DetailView):
    model = Pizza
    template_name = 'pizza_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pizzaclubs'] = Pizzaclub.objects.all()
        return context
@method_decorator(login_required, name = 'dispatch')
class PizzaDelete(DeleteView):
    model = Pizza
    template_name = 'pizza_delete_confirmation.html'
    success_url = '/pizzas/'

@method_decorator(login_required, name = 'dispatch')
class CharacterCreate(View):
    def post(self, request, pk):
        name = request.POST.get('name')
        actor = request.POST.get('actor')
        pizza = Pizza.objects.get(pk=pk)
        Character.objects.create(name=name, actor=actor, pizza=pizza)
        return redirect('pizza_detail', pk=pk)

@method_decorator(login_required, name = 'dispatch')
class PizzaclubCharacterAssoc(View):
    def get(self, request, pk, character_pk):
        assoc = request.GET.get('assoc')
        if assoc == 'remove':
            Pizzaclub.objects.get(pk=pk).characters.remove(character_pk)
        if assoc == 'add':
            Pizzaclub.objects.get(pk=pk).characters.add(character_pk)
        return redirect('/')

class Signup(View):
    def get(self, request):
        form = UserCreationForm()
        context = {'form': form}
        return render(request, 'registration/signup.html', context)
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
        else:
            context = {'form': form}
            return render(request, 'registration/signup.html', context)