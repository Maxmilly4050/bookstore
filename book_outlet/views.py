from django.shortcuts import render
from .models import Book
from django.db.models import Avg, Count

def home(request):
    books = Book.objects.all().order_by('title')
    num_books = books.count()
    book_stats = Book.objects.aggregate(avg_price=Avg('price'), total_books=Count('id'))
    return render(request, 'book_outlet/index.html', {'books': books, 'num_books': num_books, 'book_stats': book_stats})

def about(request):
    return render(request, 'book_outlet/about.html')

def book_detail(request, slug):
    book = Book.objects.get(slug=slug)
    return render(request, 'book_outlet/book_details.html', {'book': book})