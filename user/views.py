from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.decorators import login_required  
from django.shortcuts import render, get_object_or_404

from django.contrib.auth import login, authenticate, logout
from .forms import UserRegistrationForm, BooksCreationForm, AccountAuthenticationForm
from .models import (
    Users,
	Book,
    BookDetails,
)
# Create your views here.

def profile(request):
    Rform = UserRegistrationForm()
    if request.method == "POST":
        Rform = UserRegistrationForm(request.POST)
        if Rform.is_valid():
            Rform.save()
            username = Rform.cleaned_data.get('name')
            email = Rform.cleaned_data.get('email')
            messages.success(request, f'Account created! Please login to continue')
        else:
            Rform = UserRegistrationForm()


    return render(request, 'user/register.html', {'form': Rform})
   
def booksList(request):
      books = Book.objects.all()
      return render(request, 'user/booksList.html', {'books': books})

def booksCreateView(request):
    if request.method == "POST":
        try:
            Bform = BooksCreationForm(request.POST)
            if Bform.is_valid():
                Bform.save()
                return redirect('books')  # Redirect to a list of books
            else:
                messages.error(request, 'Please correct the errors below.')
        except Exception as e:
            messages.error(request, f'An error occurred: {e}')
              
    else:
        Bform = BooksCreationForm()

    return render(request, 'user/books.html', {'Bform': Bform})

def logout_view(request):
	logout(request)
	return redirect('/')


def login_view(request):

	context = {}

	user = request.user
    

	if user.is_authenticated: 
		
		return redirect("dashboard")

	if request.POST:
		form = AccountAuthenticationForm(request.POST)
		if form.is_valid():
			
			email = request.POST['email']
			user = authenticate(request, email=email)

			if user:
				login(request, user)
				return redirect("dashboard")

	else:
		form = AccountAuthenticationForm()

	context['login_form'] = form

	return render(request, "user/login.html", context)

def home_screen_view(request):
	context = {}
	return render(request, 'user/home.html', context)

def logout_view(request):
	logout(request)
	return redirect('/')

@login_required
def dashboard(request):
    
    context = {}
    return render(request, "user/dashboard.html")

def book_detail_view(request, BookID):
    book = get_object_or_404(BookDetails, Book_id=BookID)
    book_details = BookDetails.objects.all()
    return render(request, 'user/book_detail.html', {'book': book, 'book_details': book_details})