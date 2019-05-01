from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from app.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', view=index),
]+static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)