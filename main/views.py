from django.shortcuts import render
from .models import SiteContent

# Create your views here.

def home(request):
    contents = SiteContent.objects.all().order_by('-id')  # newest first
    return render(request, 'main/home.html', {'contents': contents})

def trends(request):
    return render(request, 'main/trends.html')

