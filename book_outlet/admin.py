from django.contrib import admin
from .models import Book, Author

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_filter = ('author', 'price')
    search_fields = ('title', 'author')
    list_display = ('title', 'author', 'price', 'stock')

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name')


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)