from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
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

class RahbariyatPageView(ListView):
    model = Rahbariyat
    template_name = 'rahbariyat_azolari.html'


class BayonotPageView(ListView):
    model = Bayonotlar
    template_name = 'bayonotlar.html'

class StrategiyaPageView(ListView):
    model = Harakatlar
    template_name = 'harakatlar_strategiyasi.html'
    def get_context_data(self, **kwargs):
        context = super(StrategiyaPageView, self).get_context_data(**kwargs)
        context['harakatlar'] = Harakatlar.objects.all().first()
        return context

class YangilikPageView(ListView):
    model = Yangiliklar
    template_name = 'blog/yangiliklar.html'
    def get_context_data(self, **kwargs):
        context = super(YangilikPageView, self).get_context_data(**kwargs)
        context['yangiliklar'] = Yangiliklar.objects.all().filter(active=True)
        context['categories'] = Yangiliklar_turi.objects.all()[:12]
        context['oxirgi_postlar'] = Yangiliklar.objects.all().filter(active=True).order_by('-date')[:5]
        return context

class CategoryFilterView(ListView):
    model = Yangiliklar
    template_name = 'blog/yangiliklar_filter.html'
    context_object_name = 'yangiliklar'

    def get_queryset(self):
        slug = self.kwargs['slug']
        # 1
        turi_id = Yangiliklar_turi.objects.filter(slug=slug).id
        # turi_id = Yangiliklar_turi.objects.get(slug=slug).id
        return Yangiliklar.objects.filter(turi_id=turi_id, active=True)

    # 2
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Yangiliklar_turi.objects.all()[:12]
        context['oxirgi_postlar'] = Yangiliklar.objects.filter(active=True).order_by('-date')[:5]


def single_View(request,slug):
    yangilik = get_object_or_404(Yangiliklar, slug=slug,active=True)
    context = {
        'yangilik':yangilik,
    }
    return render(request,'blog/yangiliklar_single.html',context)

