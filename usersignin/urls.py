from django.urls import path
from django.contrib import admin
from . import views
admin.autodiscover()

urlpatterns = [
    path('uploadFile/',views.upload_file),
    path('login/', views.login),
    path('regist/', views.regist),
]