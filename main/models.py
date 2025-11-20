from django.db import models
from django.contrib.auth.models import User

class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    image = models.ImageField(upload_to='services/', null=True, blank=True)

    def __str__(self):
        return self.title

class PortfolioItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='portfolio/', null=True, blank=True)

    def __str__(self):
        return self.title
