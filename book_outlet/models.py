from django.db import models
from django.utils.text import slugify

class Book(models.Model):
    title = models.CharField(max_length=200)
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField()
    slug = models.SlugField(default="", null=False, unique=True, db_index=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
