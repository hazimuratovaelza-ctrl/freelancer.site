from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services_list, name='services'),
    path('portfolio/', views.portfolio_list, name='portfolio'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('prices/', views.prices, name='prices'),
    path('account/', views.account_info, name='account'),
]
