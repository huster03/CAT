# urls.py
from django.urls import path
from .views import memory_bank_list,memory_bank_detail

urlpatterns = [
    path('memo_bank/', memory_bank_list, name='memo_bank'),
    path('memo_bank_detail/<int:memory_bank_id>/', memory_bank_detail, name='memo_bank_detail'),
    # 可以添加更多的 URL 映射
]