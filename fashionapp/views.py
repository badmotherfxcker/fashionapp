from django.shortcuts import render
from .models import Officer

# Create your views here.
def mainPage(request):
    return render(request, 'fashionapp/mainPage.html', {})