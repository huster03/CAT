from django.shortcuts import render
from .models import MemoryBankList, MemoryBankDetail
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.utils.decorators import method_decorator
from datetime import datetime


# Create your views here.
def user_certre(request):
    return render(request, 'user_centre.html')


def memory_bank_list(request):
    memory_banks = MemoryBankList.objects.all()
    return render(request, 'memo_bank.html', {'memory_banks': memory_banks})


def memory_bank_detail(request, memory_bank_id):
    memory_bank = MemoryBankDetail.objects.get(id=memory_bank_id)
    memory_bank_detail = MemoryBankDetail.objects.filter(memory_bank=memory_bank)
    paginator = Paginator(memory_bank_detail, 20)  # 在这里假设一页显示20条数据
    page = request.GET.get('page')
    memory_bank_page = paginator.get_page(page)

    return render(request, 'memo_detail.html', {'memory_bank': memory_bank, 'memory_bank_detail': memory_bank_detail,
                                                'memory_bank_page': memory_bank_page})


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
        addedMemoryData = MemoryBankDetail(source_text=add_memory_source, target_text=add_memory_target,
                                           user_id=user_id)
        addedMemoryData.save()
        # 返回一个成功的消息或者重定向到另一个页面
        return JsonResponse({'message': '记忆数据添加成功'}, status=201)  # 或者使用 redirect() 函数重定向到另一个页面


@method_decorator(csrf_exempt, name='dispatch')
def create_memory_bank(request):
    if request.method == 'POST':
        # 接收前端发送过来的数据
        data = json.loads(request.body)
        name = data.get('name')
        source_language = data.get('source_language')
        target_language = data.get('target_language')
        try:
            generated_date = datetime.now()

            new_memory_bank = MemoryBankList(name=name, source_language=source_language,
                                             target_language=target_language, generated_date=generated_date)
            new_memory_bank.save()
            # 返回创建成功的消息
            return JsonResponse({'message': '记忆库创建成功'}, status=201)
        except Exception as e:
            # 返回创建失败的消息
            return JsonResponse({'error': '记忆库创建失败: {}'.format(str(e))}, status=500)

    else:
        # 如果不是POST请求，返回错误消息
        return JsonResponse({'error': '只支持POST请求'}, status=400)
