from django.urls import path

from django.test import TestCase

from Asosiy.views import (
    HomePageView,
    Hudud_View,
    Korrupsiya_kurashView,
    ContactPageView,
    RahbariyatPageView,
    BayonotPageView,
    StrategiyaPageView,
    YangilikPageView,
    CategoryFilterView,
    YangiliklarsingleView,
    KonfirensiyalarView,
    KonfirensiyasingleView,
    TanlovlarsingleView,
    TanlovlarView, TadbirlarView, TadbirsingleView
)

# Create your tests here.
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('hududiy_bolimlar/', Hudud_View.as_view(), name='hududiy_bolimlar'),
    path('korrupsiyaga-qarshi-kurash/', Korrupsiya_kurashView.as_view(), name='korrupsiya'),
    path("boglanish/", ContactPageView.as_view(), name='boglanish'),
    path('rahbariyat/', RahbariyatPageView.as_view(), name='rahbariyat'),
    path('bayonotlar/', BayonotPageView.as_view(), name='bayonolar'),
    path('harakatlar-strategiyasi/', StrategiyaPageView.as_view(), name='harakatlar_strategiyasi'),
    path('yangiliklar/', YangilikPageView.as_view(), name='yangiliklar'),
    path('yangiliklar/filter/<slug:slug>', CategoryFilterView.as_view(), name='yangiliklik_filter'),
    path('yangiliklar/<str:slug>', YangiliklarsingleView, name='yangilik'),
    path('konfirensiyalar/', KonfirensiyalarView.as_view(), name='konfirensiyalar'),
    path('konfirensiyalar/<str:slug>', KonfirensiyasingleView, name='konfirensiya'),
    path('tanlovlar/', TanlovlarView.as_view(), name='tanlovlar'),
    path('tanlovlar/<slug:slug>', TanlovlarsingleView, name='tanlov'),
    path('tadbirlar/', TadbirlarView.as_view(), name='tadbirlar'),
    path('tadbirlar/<slug:slug>' , TadbirsingleView, name='tadbir'),
]
