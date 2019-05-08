from django.shortcuts import render
from datetime import datetime as date
from .models import *

# Create your views here.

def index(request):
    slides = Slide.objects.all().order_by('-id')[:4]
    events = Event.objects.all().order_by('-id')[:5]
    announcements = Announcement.objects.all().order_by('-id')[:7]

    current_day = date.today().strftime("%A")
    if current_day == "Sunday":
        lessons = Lesson.objects.values('sun')
    elif current_day == "Monday":
        lessons = Lesson.objects.values('mon')
    elif current_day == "Tuesday":
        lessons = Lesson.objects.values('thu')
    elif current_day == "Wednesday":
        lessons = Lesson.objects.values("wed")
    elif current_day == "Thursday":
        lessons = Lesson.objects.values('thr')
    elif current_day == "Friday":
        lessons = Lesson.objects.values('fri')
    elif current_day == "Saturday": 
        lessons = Lesson.objects.values('sat')

    content = {
        'slides': slides,
        'events': events,
        'announcements': announcements,
        'lessons': lessons
    }

    return render(request, 'index.html', content) 
