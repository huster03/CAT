from django.shortcuts import render
from .models import MemoryBankList,MemoryBankDetail
from django.core.paginator import Paginator

# Create your views here.
def user_certre(request):
    return render(request, 'user_centre.html')

def memory_bank_list(request):
    memory_banks = MemoryBankList.objects.all()
    return render(request, 'memory_bank.html', {'memory_banks': memory_banks})

def memory_bank_detail(request, memory_bank_id):
    memory_bank = memory_bank.objects.get(id=memory_bank_id)
    try:
        memory_bank_detail = MemoryBankDetail.objects.get(memory_bank=memory_bank)
    except MemoryBankDetail.DoesNotExist:
        memory_bank_detail = None
    paginator = Paginator(memory_bank_detail, 20)  # 在这里假设一页显示20条数据
    page = request.GET.get('page')
    memory_bank_page = paginator.get_page(page)

    return render(request, 'memory_bank_detail.html', {'memory_bank': memory_bank, 'memory_bank_detail': memory_bank_detail, 'memory_bank_page': memory_bank_page})


def searchMemoryData(request):
    if request.method == 'GET':
        query_memory = request.GET.get('query_memory', '')
        MemoryDatas = MemoryBankDetail.objects.filter(source_text__icontains=query_memory)
        return {'MemoryDatas': MemoryDatas, 'query_memory': query_memory}

    return {}

def addMemoryData(request, user_id):
    if request.method == "POST" and 'add_memory_source' in request.POST:
        add_memory_source = request.POST.get('add_memo_source')
        add_memory_target = request.POST.get('add_memo_target')
        addedMemoryData = MemoryBankDetail(source_text=add_memory_source, target_text=add_memory_target, user_id=user_id)
        addedMemoryData.save()
