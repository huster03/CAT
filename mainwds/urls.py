from django.urls import path
from django.contrib import admin
from . import views

admin.autodiscover()

urlpatterns = [
    path('main_display/<str:project_name>/', views.main_display, name="main_display"),
    path('translate/', views.translate, name='translate'),
    path('ajax/', views.ajax_match_strings, name='ajax_match_strings'),
    # 其他 URL 配置
]
