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
        context['oxirgi_postlar'] = Yangiliklar.objects.all().filter(active=True).order_by('-publish_time')[:5]
        return context

# class CategoryFilterView(ListView):
#     model = Yangiliklar
#     template_name = 'blog/yangiliklar_filter.html'
#     context_object_name = 'yangiliklar'
#
#     def get_queryset(self):
#         slug = self.kwargs['slug']
#         # 1
#         turi_id = Yangiliklar_turi.objects.filter(slug=slug).id
#         # turi_id = Yangiliklar_turi.objects.get(slug=slug).id
#         return Yangiliklar.objects.filter(turi_id=turi_id, active=True)
#
#     # 2
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['categories'] = Yangiliklar_turi.objects.all()[:12]
#         context['oxirgi_postlar'] = Yangiliklar.objects.filter(active=True).order_by('-date')[:5]
class CategoryFilterView(ListView):
    model = Yangiliklar
    template_name = 'blog/yangiliklar_filter.html'
    context_object_name = 'yangiliklar'

    def get_queryset(self):
        slug = self.kwargs['slug']
        turi_id = Yangiliklar_turi.objects.get(slug=slug).id
        return Yangiliklar.objects.filter(turi_id=turi_id, active=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Yangiliklar_turi.objects.all()[:12]
        context['oxirgi_postlar'] = Yangiliklar.objects.filter(active=True).order_by('-date')[:5]
        return context

def YangiliklarsingleView(request,slug):
    yangilik = get_object_or_404(Yangiliklar, slug=slug,active=True)
    oxirgi_postlar = Yangiliklar.objects.filter(active=True).order_by('-date')[:4]
    context = {
        'yangilik':yangilik,
        'oxirgi_postlar':oxirgi_postlar,
    }
    return render(request,'blog/yangiliklar_single.html',context)

class KonfirensiyalarView(ListView):
    model = Konfirensiya
    template_name = 'blog/blog-konfirensiyalar.html'
    def get_context_data(self, **kwargs):
        context = super(KonfirensiyalarView, self).get_context_data(**kwargs)
        context['konfirensiyalar'] = Konfirensiya.objects.all().filter(active=True)
        context['oxirgi_postlar'] = Konfirensiya.objects.all().filter(active=True).order_by('-publish_time')[:5]
        return context

def KonfirensiyasingleView(request,slug):
    yangilik = get_object_or_404(Konfirensiya, slug=slug,active=True)
    oxirgi_postlar = Konfirensiya.objects.filter(active=True).order_by('-boshlanish_sanasi')[:4]
    context = {
        'yangilik':yangilik,
        'oxirgi_postlar':oxirgi_postlar,
    }
    return render(request,'blog/konfirensiya_detail.html',context)

class TanlovlarView(ListView):
    model = Tanlov
    template_name = 'blog/blog-tanlovlar.html'
    def get_context_data(self, **kwargs):
        context = super(TanlovlarView, self).get_context_data(**kwargs)
        context['tanlovlar'] = Tanlov.objects.all().filter(active=True)
        context['oxirgi_postlar'] = Tanlov.objects.all().filter(active=True)[:5]
        return context

def TanlovlarsingleView(request,slug):
    tanlov = get_object_or_404(Tanlov, slug=slug,active=True)
    oxirgi_postlar = Tanlov.objects.filter(active=True)[:4]
    context = {
        'tanlov':tanlov,
        'oxirgi_postlar':oxirgi_postlar,
    }
    return render(request,'blog/tanlov_detail.html',context)

class TadbirlarView(ListView):
    model = Tadbir
    template_name = 'blog/blog-tadbirlar.html'
    def get_context_data(self, **kwargs):
        context = super(TadbirlarView, self).get_context_data(**kwargs)
        context['tadbirlar'] = Tadbir.objects.all().filter(active=True)
        context['oxirgi_postlar'] = Tadbir.objects.all().filter(active=True)[:5]
        return context

def TadbirsingleView(request,slug):
    tadbir = get_object_or_404(Tadbir, slug=slug,active=True)
    context = {
        'tadbir':tadbir,
    }
    return render(request,'blog/tadbir_detail.html',context)

class GaleryView(ListView):
    model = Rasmlar
    template_name = 'gallery.html'
    def get_context_data(self, **kwargs):
        context = super(GaleryView, self).get_context_data(**kwargs)
        context['categories'] = Rasmlar_turlari.objects.all()[:8]
        return context

class GaleryFilterView(ListView):
    model = Rasmlar
    template_name = 'gallery-filter.html'
    context_object_name = 'rasmlar'

    def get_queryset(self):
        slug = self.kwargs['slug']
        turi_id = Rasmlar_turlari.objects.get(slug=slug).id
        return Rasmlar.objects.filter(turi_id=turi_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Rasmlar_filtered'] = Rasmlar.objects.all()
        context['categories'] = Rasmlar_turlari.objects.all()[:8]
        return context





