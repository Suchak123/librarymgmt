from django.urls import path
from .views import (
    CreateUserAPIView, 
    ListAllUsersAPIView, 
    GetUserByIDAPIView,
    CreateBookAPIView,
    ListAllBooksAPIView,
    GetBookByIDAPIView,
    assign_update_book_details,
    BorrowBookAPIView,
    ReturnBookAPIView,
    ListBorrowedBooksAPIView
)
from django.contrib.auth import views as auth_views

app_name = 'user'
urlpatterns = [
    path('users/create/', CreateUserAPIView.as_view(), name='create-user'),
    path('users/list/', ListAllUsersAPIView.as_view(), name='list-users'),
    path('users/<int:userId>/', GetUserByIDAPIView.as_view(), name='get-user-by-id'),
    path('books/create/', CreateBookAPIView.as_view(), name='create-user'),
    path('books/list/', ListAllBooksAPIView.as_view(), name='list-users'),
    path('books/<int:BookID>/', GetBookByIDAPIView.as_view(), name='get-book-by-id'),
    path('books/<int:book_id>/details/', assign_update_book_details, name='assign-update-book-details'),
    path('books/borrow/', BorrowBookAPIView.as_view(), name='borrow-book'),
    path('books/return/<int:BookID>', ReturnBookAPIView.as_view(), name='return-book'),
    path('borrowed/list/', ListBorrowedBooksAPIView.as_view(), name='list-borrowed-books'),
]
