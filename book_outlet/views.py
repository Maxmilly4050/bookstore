from django.shortcuts import render
from .models import Book

def home(request):
    books = Book.objects.all()
    return render(request, 'book_outlet/index.html', {'books': books})

def about(request):
    return render(request, 'book_outlet/about.html')

def book_detail(request, slug):
    book = Book.objects.get(slug=slug)
    return render(request, 'book_outlet/book_details.html', {'book': book})