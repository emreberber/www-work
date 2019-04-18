from django.conf.urls import url
from django.contrib import admin
from app.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', view=index),
]
