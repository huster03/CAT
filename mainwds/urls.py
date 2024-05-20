from django.urls import path
from django.contrib import admin
from . import views
admin.autodiscover()

urlpatterns = [
    path('main_display/', views.main_display,name = "main_display"),
]