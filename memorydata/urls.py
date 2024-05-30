# urls.py
from django.urls import path
from .views import user_certre,memory_bank_list,memo_bank_detail

urlpatterns = [
    path('user_centre/', user_certre, name='user_centre'),
    path('memo_bank/', memory_bank_list, name='memo_bank'),
    path('memo_bank_detail/<int:memory_bank_id>/', memo_bank_detail, name='memo_bank_detail'),
    # 可以添加更多的 URL 映射
]