from django.http import HttpResponse
from django.shortcuts import render

def home_screen_view(request):
    context = {}
    return render(request, 'user/home.html', context)