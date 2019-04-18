from django.db import models

# Create your models here.

class Slide(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=120)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Event(models.Model):
    title  = models.CharField(max_length=120)
    date   = models.CharField(max_length=120)
    place  = models.CharField(max_length=120)
    detail = models.TextField()

    def __str__(self):
        return self.title

class Lesson(models.Model):
    sun = models.TextField()
    mon = models.TextField()
    thu = models.TextField()
    wed = models.TextField()
    thr = models.TextField()
    fri = models.TextField()
    sat = models.TextField()

    def __str__(self):
        return "Lessons"

class Announcement(models.Model):
    title = models.CharField(max_length=120)
    text  = models.TextField()

    def __str__(self):
        return self.title

        