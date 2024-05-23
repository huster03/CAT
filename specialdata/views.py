from django.shortcuts import render
from .models import TermBankList, TermBankDetail
# Create your views here.
def term_bank_interface(request):
    # 获取术语库列表
    term_banks = TermBankList.objects.all()

    # 将术语库列表传递给模板
    return render(request, 'term_bank_interface.html', {'term_banks': term_banks})

def search_term_bank(request):
    # 处理搜索逻辑
    keyword = request.GET.get('keyword', '')

    # 在后端进行搜索逻辑（这里假设你有对应的搜索函数）

    # 返回搜索结果
    search_results = []  # 假设这个是你搜索的结果
    return JsonResponse({'search_results': search_results})