from django.contrib import admin

# Register your models here.

from .models import Slide, Event, Lesson, Announcement
admin.site.register(Slide)
admin.site.register(Event)
admin.site.register(Lesson)
admin.site.register(Announcement)
