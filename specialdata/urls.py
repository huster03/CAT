# urls.py
from django.urls import path
from .views import term_bank_interface, search_term_bank

urlpatterns = [
    path('term_bank_interface/', term_bank_interface, name='term_bank_interface'),
    path('search_term_bank/', search_term_bank, name='search_term_bank'),
    # 可以添加更多的 URL 映射
]