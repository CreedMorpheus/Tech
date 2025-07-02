from django.shortcuts import render
from .models import SiteContent

# Create your views here.

def home(request):
    content = SiteContent.objects.last()
    return render(request, 'main/home.html', {'content': content})

def trends(request):
    return render(request, 'main/trends.html')

