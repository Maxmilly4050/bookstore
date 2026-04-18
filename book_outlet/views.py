from django.shortcuts import render

def home(request):
    return render(request, 'book_outlet/index.html')

def about(request):
    return render(request, 'book_outlet/about.html')