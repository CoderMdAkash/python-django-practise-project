from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='index'),
    path('about', views.about, name='about'),
    path('form', views.form, name='form'),
    path('form-action', views.formAction, name='formAction'),
]
