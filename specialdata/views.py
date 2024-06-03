from django.shortcuts import render
from django.http import JsonResponse
from .models import TermBankList ,TermBankItem
from django.core.paginator import Paginator
from usersignin.models import User
# Create your views here.
def term_bank_list(request):
    username = request.session.get('username')
    user = User.objects.get(username=username)
    user_id = user.id
    term_banks = TermBankList.objects.filter(user_id = user_id)
    # 将术语库列表传递给模板
    return render(request, 'tech_bank.html', {'term_banks': term_banks , 'username':username})


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
        addedSpecialData = TermBankItem(source_text=add_special_source, target_text=add_special_target,
                                            user_id=user_id)
        addedSpecialData.save()
    # 返回搜索结果
    search_results = []  # 假设这个是你搜索的结果
    return JsonResponse({'search_results': search_results})

def term_bank_detail(request, term_bank_id):
    # 获取术语库详情
    username = request.session.get('username')
    user = User.objects.get(username=username)
    user_id = user.id
    term_bank_detail = TermBankItem.objects.filter(term_bank_id=term_bank_id,user_id = user_id)
    # paginator = Paginator(term_bank_details, 20)  # 在这里假设一页显示20条数据
    # page = request.GET.get('page')
    # term_bank_page = paginator.get_page(page)
    # 将术语库详情传递给模板
    return render(request, 'tech_detail.html', {'term_bank_detail': term_bank_detail,'username':username})