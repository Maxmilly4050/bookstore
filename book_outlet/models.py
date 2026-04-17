from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return self.title
