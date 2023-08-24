from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='index'),
    path('about', views.about, name='about'),
    path('form', views.form, name='form'),
    path('form-action', views.formAction, name='formAction'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
