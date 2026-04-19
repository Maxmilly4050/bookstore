from django.db import models
from django.utils.text import slugify

class Book(models.Model):
    title = models.CharField(max_length=200)
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    author = models.ForeignKey('Author', on_delete=models.CASCADE, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField()
    slug = models.SlugField(default="", null=False, db_index=True, editable=False)
    description = models.TextField(blank=True)
    published_countries = models.ManyToManyField('Country', blank=True)

    def __str__(self):
        return self.title
    
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    Address = models.OneToOneField('Address', on_delete=models.CASCADE, null=True, related_name='author')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Address(models.Model):
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.street}, {self.city}, {self.state} {self.zip_code}"
    
    class Meta:
        verbose_name_plural = "Addresses"

class Country(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Countries"