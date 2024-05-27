# urls.py
from django.urls import path
from .views import user_certre,memo_bank,memo_bank_detail

urlpatterns = [
    path('user_centre/', user_certre, name='user_centre'),
    path('memo_bank/', memo_bank, name='memo_bank'),
    path('memo_bank_detail/<int:memo_id>/', memo_bank_detail, name='memo_bank_detail'),
    # 可以添加更多的 URL 映射
]