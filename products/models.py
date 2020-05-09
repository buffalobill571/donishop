from django.db import models


class Company(models.Model):
    name = models.TextField()
    image = models.ImageField(null=True, blank=True)


class Product(models.Model):
    company = models.ForeignKey(Company, related_name='products', null=True, blank=True)

    name = models.TextField()

    image = models.ImageField(null=True, blank=True)
