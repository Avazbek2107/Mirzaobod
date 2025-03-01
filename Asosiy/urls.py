from django.urls import path

from django.test import TestCase

from Asosiy.views import (
    HomePageView,
    Hudud_View, Korrupsiya_kurashView, ContactPageView,

)
# Create your tests here.
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('hududiy_bolimlar/', Hudud_View.as_view(), name='hududiy_bolimlar'),
    path('korrupsiyaga-qarshi-kurash/', Korrupsiya_kurashView.as_view(), name='korrupsiya'),
    path("boglanish/", ContactPageView.as_view(), name='boglanish'),
]