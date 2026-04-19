from django.contrib import admin
from .models import Book

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('author', 'price')
    search_fields = ('title', 'author')
    list_display = ('title', 'author', 'price', 'stock')


admin.site.register(Book, BookAdmin)