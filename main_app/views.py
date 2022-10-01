from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
# Create your views here.

class Home(TemplateView):
    template_name = 'home.html'

class About(TemplateView):
    template_name = 'about.html'

class Pizzas(TemplateView):
    template_name = 'pizzas.html'

class Pizza:
    def __init__(self, image, name, review):
        self.image = image
        self.name = name
        self.review = review


pizzas = [
    Pizza("https://i.imgur.com/WzN9pUg.png", "Ninja Turtles Cartoon" "It's really hard to judge the quality here, being a cartoon. 5/10. Nice, safe score"),
    Pizza("https://i.imgur.com/wVLs8kN.png", "Ninja Turles movie", "Gross. Why are these denizens of NYC eathing Domino's? 0/10"),
    Pizza("https://i.imgur.com/585Lnod.png", "Saturday Night Fever", "You only get a quick glimpse, but the pizza looks good. More importantly, you can tell by the way he eats his pizza (two slices at a time), he's a business man, no time for talk. 10/10 for pizza and technique."),
    Pizza("https://i.imgur.com/fglYdAt.png", "Back to the Future II", "It looks exactly like you would expect pizza that came out of a weird futuristic appliance to look. 5/10"),
    Pizza("https://i.imgur.com/09rQK55.png", "Sex and the City", "Bad show, good looking pizza. At least they eat their pizza at a real NY slice joint. 10/10"),
    Pizza("https://i.imgur.com/jlDa3kY.png", "Fast Times at Ridgemont High", "It honestly looks pretty good for cali pizza. 7/10"),
    Pizza("https://i.imgur.com/rrj8pEE.png", "Mystic Pizza", "I'm not a huge topping guy, but you can't argue with a classic supreme, which is apparently what a Mystic Pizza is. Can't see enough to really judge the rest of it. Let's go with 6/10"),
    Pizza("https://i.imgur.com/FoXoLM7.png", "Eat, Pray, Love", "Dumb book, probably bad movie, but that real Neopolitan pizza looks delish! 10/10"),
    Pizza("https://i.imgur.com/6TWDCiE.png", "Do the Right Thing", "Hard to see, but it's gotta be good. It's Brooklyn. 8/10"),
    Pizza("https://i.imgur.com/h7lVEJh.png", "Breaking Bad", "It honestly looks really good considering it's in New Mexico, and it's on a roof. 7/10"),
    Pizza("https://i.imgur.com/wo5lvWA.png", "Kramer's custom pizza", "You can't see the pizza her. In fact, I don't think Kramer's pizza ever gets made. This is a tough one. I agree with Papi, as a pizza purist. Cucumbers don't belong. But I also agree with Kramer's philosophy of no bounds on creativity. The problem is that, speaking from experience in the ice cream biz, customers will make something gross and blame it on the establishment. 3/10"),
    Pizza("https://i.imgur.com/c0DLSbz.png", "Rock 'n' Roll High School", "Again, you can't really see it, but I'm gonna trust that the Ramones wouldn't eat bad pizza. 8/10"),
    Pizza("https://i.imgur.com/bRpjOce.png", "E.T.", "This is Cali pizza, so it's probaby better after it was dropped on the ground. 2/10"),
    Pizza("https://i.imgur.com/xmyuVyW.jpg", "Inside Out", "I think a white pizza with broccoli certainly  has its place. But I have to object to the cucumbers (again) and what looks like maybe asparagus. 5/10")
]