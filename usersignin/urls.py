from django.urls import path
from django.contrib import admin
from . import views
admin.autodiscover()

urlpatterns = [
    path('uploadFile/',views.upload_file , name ='uploadFile'),
    path('login/', views.login , name = 'login'),
    path('regist/', views.regist,name = 'regist'),
]