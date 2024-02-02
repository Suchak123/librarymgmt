from django.db import models
from django.utils import timezone
# from django.contrib.auth.models import User

# Create your models here.
class Users(models.Model):
    userId = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 50, null = True, unique = True)
    email = models.EmailField(max_length = 30, null = True, unique = True)
    membershipDate = models.DateField(null = True, default = timezone.now)

    def __str__(self) :
        return self.name 
# 

class Book(models.Model):
    BookID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    ISBN = models.CharField(max_length=13, unique=True)
    publishedDate = models.DateField(null = True, default = timezone.now)
    genre = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class BookDetails(models.Model):
    DetailsID = models.AutoField(primary_key=True)
    Book = models.OneToOneField(Book, on_delete=models.CASCADE)
    NumberOfPages = models.IntegerField()
    Publisher = models.CharField(max_length=255)
    Language = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.Book.title} Details"

class BorrowedBooks(models.Model):
    UserID = models.ForeignKey(Users, on_delete=models.CASCADE, db_column='userId')
    BookID = models.ForeignKey(Book, on_delete=models.CASCADE, db_column='BookID')
    BorrowDate = models.DateField()
    ReturnDate = models.DateField(null=True)

    def __str__(self):
        return f"{self.Users.userId} - {self.Book.BookID} Borrowed"    