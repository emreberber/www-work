from django.db import models

# Create your models here.

class Slide(models.Model):
    image = models.FileField(null=False, blank=False)
    title = models.CharField(max_length=240)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Event(models.Model):
    title  = models.CharField(max_length=480)
    date   = models.CharField(max_length=480, null=True, blank=True)
    place  = models.CharField(max_length=480, null=True, blank=True)
    detail = models.TextField()

    def __str__(self):
        return self.title

class Lesson(models.Model):
    sun = models.TextField(verbose_name="Sunday")
    mon = models.TextField(verbose_name="Monday")
    thu = models.TextField(verbose_name="Tuesday")
    wed = models.TextField(verbose_name="Wednesday")
    thr = models.TextField(verbose_name="Thursday")
    fri = models.TextField(verbose_name="Friday")
    sat = models.TextField(verbose_name="Saturday")

    def __str__(self):
        return "Lessons"

class Announcement(models.Model):
    title = models.CharField(max_length=480)
    text  = models.TextField()

    def __str__(self):
        return self.title

        