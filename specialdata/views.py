from django.shortcuts import render
from django.http import JsonResponse
from .models import TermBankList, TermBankDetail
from django.core.paginator import Paginator
# Create your views here.
def term_bank_list(request):
    # 获取术语库列表
    term_banks = TermBankList.objects.all()

    # 将术语库列表传递给模板
    return render(request, 'tech_bank.html', {'term_banks': term_banks})


def search_term_bank(request):
    if request.method == 'GET':
        query_special = request.GET.get('query_special', '')
        if query_special is not None:
            term_bank_lists = TermBankList.objects.filter(source_text__icontains=query_special)
            return {'TermBankLists': term_bank_lists, 'query_special': query_special}

    return {}

def add_term_bank(request, user_id):
    if request.method == "POST" and 'add_special_source' in request.POST:
        add_special_source = request.POST.get('add_special_source')
        add_special_target = request.POST.get('add_special_target')
        addedSpecialData = TermBankDetail(source_text=add_special_source, target_text=add_special_target,
                                            user_id=user_id)
        addedSpecialData.save()
    # 返回搜索结果
    search_results = []  # 假设这个是你搜索的结果
    return JsonResponse({'search_results': search_results})

def term_bank_detail(request, term_bank_id):
    # 获取术语库详情
    term_bank = TermBankList.objects.get(id=term_bank_id)
    term_bank_details = TermBankDetail.objects.filter(term_bank=term_bank)
    paginator = Paginator(term_bank_details, 20)  # 在这里假设一页显示20条数据
    page = request.GET.get('page')
    term_bank_page = paginator.get_page(page)

    # 将术语库详情传递给模板
    return render(request, 'tech_bank_detail.html', {'term_bank': term_bank, 'term_bank_details': term_bank_details, 'term_bank_page': term_bank_page})