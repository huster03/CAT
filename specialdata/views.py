from django.shortcuts import render
from django.http import JsonResponse
from .models import TermBankList, TermBankDetail
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