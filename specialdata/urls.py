# urls.py
from django.urls import path
from .views import term_bank_list, search_term_bank

urlpatterns = [
    path('term_bank/', term_bank_list, name='term_bank_list'),
    path('term_detail/', search_term_bank, name='search_term_bank'),
    # 可以添加更多的 URL 映射
]