"""
URL configuration for problem_2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.http import HttpResponse

# Temporary root view
def home_view(request):
    return HttpResponse("<h1>Welcome to the Django Project!</h1>")

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel
    path('', include('problem2.urls')),  # App-specific URLs
    #path('', home_view, name='home'),  # Root URL pattern
]