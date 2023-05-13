from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'info-home'),
    path('education/', views.education, name = 'info-education'),
    path('compage/', views.compage, name = 'info-compage'),
    path('chen/', views.chen, name = 'info-chen'),
    path('liu/', views.liu, name = 'info-liu'),
    path('xu/', views.xu, name = 'info-xu'),
    path('contact/', views.contact, name = 'info-contact'),
    path('camppage/', views.camppage, name = 'info-camppage'),
    path('signup/', views.tarif, name = 'info-tarif'),




]
