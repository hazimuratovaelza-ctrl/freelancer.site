from django.shortcuts import render
from .models import Service, PortfolioItem

def home(request):
    services = Service.objects.all()[:6]
    portfolio = PortfolioItem.objects.all()[:6]
    return render(request, 'home.html', {'services': services, 'portfolio': portfolio})

def services_list(request):
    services = Service.objects.all()
    return render(request, 'services.html', {'services': services})

def portfolio_list(request):
    items = PortfolioItem.objects.all()
    return render(request, 'portfolio.html', {'items': items})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def prices(request):
    services = Service.objects.all()
    return render(request, 'prices.html', {'services': services})

def account_info(request):
    return render(request, 'account.html')

