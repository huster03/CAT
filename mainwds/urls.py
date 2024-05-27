from django.urls import path
from django.contrib import admin
from . import views
admin.autodiscover()

urlpatterns = [
    path('main_display/<str:project_name>/', views.main_display,name = "main_display"),
]