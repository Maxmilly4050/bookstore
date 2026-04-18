from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('<slug:slug>/', views.book_detail, name='book_detail'),
]