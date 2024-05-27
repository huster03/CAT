from django.shortcuts import render
from .models import MemoryBankList,MemoryBankDetail

# Create your views here.
def user_certre(request):
    return render(request, 'user_centre.html')
def memo_bank(request):
    return render(request, 'memo_bank.html')

def searchMemoryData(request):
    if request.method == 'GET':
        query_memory = request.GET.get('query_memory', '')
        MemoryDatas = MemoryBankDetail.objects.filter(source_text__icontains=query_memory)
        return {'MemoryDatas': MemoryDatas, 'query_memory': query_memory}

    return {}

def addMemoryData(request, user_id):
    if request.method == "POST" and 'add_memory_source' in request.POST:
        add_memory_source = request.POST.get('add_memory_source')
        add_memory_target = request.POST.get('add_memory_target')
        addedMemoryData = MemoryBankDetail(source_text=add_memory_source, target_text=add_memory_target, user_id=user_id)
        addedMemoryData.save()
