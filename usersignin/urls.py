from django.urls import path
from django.contrib import admin
from . import views
admin.autodiscover()

urlpatterns = [
    path('login/', views.login , name = 'login'),
    path('regist/', views.regist,name = 'regist'),
    path('uer_centre/', views.user_centre, name='user_centre'),
]