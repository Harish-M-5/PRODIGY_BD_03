from django.http import HttpResponse
from django.contrib import admin
from django.urls import path, include

def home(request):
    return HttpResponse("Welcome to Harish API 🚀 — Go to /api/ for users list!")

urlpatterns = [
    path('', home),  # 👈 add this line
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
]
