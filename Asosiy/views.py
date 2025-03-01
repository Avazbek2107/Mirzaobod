from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, FormView

from .form import ContactForm
from .models import *

# Create your views here.

class HomePageView(ListView):
    model = Togaraklar
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['togaraklar'] = Togaraklar.objects.all().filter(active=True)[:3]
        context['ochiq_budjet'] = Budjet.objects.all().filter(active=True)[:4]
        context['oxirgi_ishlar'] = Oxirgi_ishlar.objects.all().filter(active=True)[:3]
        context['rahbariyat'] = Rahbariyat.objects.all()[:4]
        return context

class Hudud_View(ListView):
    model = Hududiy_Rahbariyat
    template_name = 'hududiy_bolimlar.html'

    def get_context_data(self, **kwargs):
        context = super(Hudud_View, self).get_context_data(**kwargs)
        context['number'] = Numbers.objects.first()
        context["rahbarlar"] = Hududiy_Rahbariyat.objects.all()[:3]
        return context

class Korrupsiya_kurashView(ListView):
    model = Korrupsiya_kurash
    template_name = 'korrupsiya_kurash.html'
    def get_context_data(self, **kwargs):
        context = super(Korrupsiya_kurashView, self).get_context_data(**kwargs)
        context['Korrupsiyalar'] = Korrupsiya_kurash.objects.all().filter(active=True)[:3]
        # print(context["korrupsiyalar"])
        return context

class ContactPageView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return redirect('home')
