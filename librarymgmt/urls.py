"""
URL configuration for librarymgmt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings 

from user.views import (
    profile,
   
    login_view,
    home_screen_view,
    logout_view,
    dashboard,
    booksCreateView,
    booksList,
    book_detail_view

)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', profile, name='register'),
    path('books/', booksCreateView, name='books'),
    path('booksList/', booksList, name='booksList'),
    path('login/', login_view, name='login'),
    path('', home_screen_view, name="home"),
    path('logout/', logout_view, name="logout"),
    path('dashboard/', dashboard, name="dashboard"),
    path('api/', include('user.api.urls', 'user_api')),
    
]
