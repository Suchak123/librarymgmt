from rest_framework import serializers
from user.models import Users, Book, BookDetails, BorrowedBooks

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['userId', 'name', 'email', 'membershipDate']

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['BookID', 'title', 'ISBN', 'publishedDate', 'genre']

class BookDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookDetails
        fields = ['DetailsID', 'NumberOfPages', 'Publisher', 'Language']


class BorrowedBooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowedBooks
        fields = ['UserID', 'BookID', 'BorrowDate', 'ReturnDate']        