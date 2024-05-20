from django import forms
from django.http import JsonResponse
from django.shortcuts import render
from usersignin.models import User
from memorydata.models import Memorydatatable
from specialdata.models import Specialdatatable
from usersignin.models import  TextTranslationPart
import json

context = {}


class UploadFileForm(forms.Form):
    file = forms.FileField()

def get_translation_data(username):
    parts = TextTranslationPart.objects.filter(username=username).order_by('part_index')
    if parts:
        source_text_list = [part.source_text for part in parts]
        target_text_list = [part.target_text for part in parts]
        return source_text_list, target_text_list
    else:
        return None, None

def updateMysqldata(request,username):
    if request.META.get('CONTENT_TYPE') == 'application/json':
        translated_content = json.loads(request.body)
        parts = TextTranslationPart.objects.filter(username=username)
        for i, part in enumerate(parts):
            part.target_text = translated_content[i]
            part.save()
    else:
        pass
def display_translation(request, username):
    form = UploadFileForm()
    target_text_list = None
    source_text_list = None
    source_text_lists, target_text_lists = get_translation_data(username)
    source_text_list = json.dumps(source_text_lists)
    target_text_list = json.dumps(target_text_lists)
    return {'form': form, 'username': username, 'source_text_list': source_text_list,
            'target_text_list': target_text_list}

def searchMemoryData(request):
    if request.method == 'GET':
        query_memory = request.GET.get('query_memory', '')
        MemoryDatas = Memorydatatable.objects.filter(source_text__icontains=query_memory)
        return {'MemoryDatas': MemoryDatas, 'query_memory': query_memory}

    return {}


def searchSpecialData(request):
    if request.method == 'GET':
        query_special = request.GET.get('query_special', '')
        if query_special is not None:
            SpecialDatas = Specialdatatable.objects.filter(source_text__icontains=query_special)
            return {'SpecialDatas': SpecialDatas, 'query_special': query_special}

    return {}


def addMemoryData(request, user_id):
    if request.method == "POST" and 'add_memory_source' in request.POST:
        add_memory_source = request.POST.get('add_memory_source')
        add_memory_target = request.POST.get('add_memory_target')
        addedMemoryData = Memorydatatable(source_text=add_memory_source, target_text=add_memory_target, user_id=user_id)
        addedMemoryData.save()


def addSpecialData(request, user_id):
    if request.method == "POST" and 'add_special_source' in request.POST:
        add_special_source = request.POST.get('add_special_source')
        add_special_target = request.POST.get('add_special_target')
        addedSpecialData = Specialdatatable(source_text=add_special_source, target_text=add_special_target,
                                            user_id=user_id)
        addedSpecialData.save()


def main_display(request):
    username = request.session.get('username')
    user = User.objects.get(username=username)
    user_id = user.id
    updateMysqldata(request,username)
    context.update(display_translation(request, username))
    context.update(searchMemoryData(request))
    context.update(searchSpecialData(request))
    addMemoryData(request, user_id)
    addSpecialData(request, user_id)
    return render(request, 'main_display.html', context)
