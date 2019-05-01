from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    slides = Slide.objects.all()
    content = {
        'slides': slides
    }

    return render(request, 'index.html', content) 
