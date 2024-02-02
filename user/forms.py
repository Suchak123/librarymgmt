from django import forms
from django.utils import timezone
from .models import (
    Users,
	Book,
	
)
from django.contrib.auth import authenticate
class UserRegistrationForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = Users
        fields = ['name', 'email']

class BooksCreationForm(forms.ModelForm):
    title = forms.CharField(required=True)
    ISBN = forms.CharField(required=True)
    publishedDate = forms.DateField(initial = timezone.now)
    genre = forms.CharField(required=False)     

    class Meta:
        model = Book
        fields = ['title', 'ISBN', 'publishedDate', 'genre']

class AccountAuthenticationForm(forms.ModelForm):

	password = forms.CharField(label='Password', widget=forms.PasswordInput)

	class Meta:
		model = Users
		fields = ('email', 'password')

	def clean(self):
		if self.is_valid():
			email = self.cleaned_data['email']
			password = self.cleaned_data['password']
			if not authenticate(email=email, password=password):
				raise forms.ValidationError("Invalid login")