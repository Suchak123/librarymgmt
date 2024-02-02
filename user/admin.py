from django.contrib import admin
from django.contrib.auth.models import User
from .models import (
    Users,
    Book,
    BookDetails,
    BorrowedBooks,
)
# Register your models here.
admin.site.register(Users)
admin.site.register(Book)
admin.site.register(BookDetails)

class UsersAdmin(admin.ModelAdmin):
    list_display = ('userId', 'name', 'email')

class BorrowedBooksAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'BorrowDate', 'ReturnDate')

    def user(self, obj):
        return obj.UserID.name

    def book(self, obj):
        return obj.BookID.title   

admin.site.register(BorrowedBooks, BorrowedBooksAdmin)
