# urls.py
from django.urls import path
from .views import term_bank_list, search_term_bank
from . import views

urlpatterns = [
    path('term_bank/', term_bank_list, name='term_bank'),
    path('term_detail/', search_term_bank, name='term_detail'),
    path('term_bank_detail/<int:term_bank_id>/', views.term_bank_detail, name='term_bank_detail'),
    # 可以添加更多的 URL 映射
]