from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from user.models import Users, Book, BorrowedBooks
from rest_framework.decorators import api_view
from django.utils import timezone

from .serializers import UserSerializer, BookSerializer, BookDetailsSerializer, BorrowedBooksSerializer

class CreateUserAPIView(generics.CreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer

class ListAllUsersAPIView(generics.ListAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer

class GetUserByIDAPIView(generics.RetrieveAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'userId'


class CreateBookAPIView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class ListAllBooksAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class GetBookByIDAPIView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'BookID'

@api_view(['PUT'])
def assign_update_book_details(request, book_id):
    book = Book.objects.get(BookID=book_id)
    
    if request.method == 'PUT':
        serializer = BookDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(Book=book)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class BorrowBookAPIView(generics.CreateAPIView):
    queryset = BorrowedBooks.objects.all()
    serializer_class = BorrowedBooksSerializer

class ReturnBookAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BorrowedBooks.objects.all()
    serializer_class = BorrowedBooksSerializer
    lookup_field = 'BookID'  
     

    def perform_update(self, serializer):
        serializer.is_valid(raise_exception=True)

        book_id = self.kwargs['pk']
        borrowed_books = BorrowedBooks.objects.filter(BookID=book_id, ReturnDate__isnull=True)

        borrowed_book = get_object_or_404(borrowed_books)

        serializer.save(ReturnDate=None)
    

class ListBorrowedBooksAPIView(generics.ListAPIView):
    queryset = BorrowedBooks.objects.all()
    serializer_class = BorrowedBooksSerializer    