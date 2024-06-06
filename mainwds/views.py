from django import forms
from django.http import JsonResponse
from django.shortcuts import render
from usersignin.models import User
from usersignin.models import TextTranslationPart
import json
from .translation import connect
from django.http import JsonResponse
from fuzzywuzzy import fuzz

context = {}


class UploadFileForm(forms.Form):
    file = forms.FileField()


def get_translation_data(username, project_name):
    parts = TextTranslationPart.objects.filter(username=username, project_name=project_name).order_by('part_index')
    if parts:
        source_text_list = [part.source_text for part in parts]
        target_text_list = [part.target_text for part in parts]
        return source_text_list, target_text_list
    else:
        return None, None


def updateMysqldata(request, username, project_name):
    if request.META.get('CONTENT_TYPE') == 'application/json':
        translated_content = json.loads(request.body)
        print(translated_content)
        print(username)
        print(project_name)
        parts = TextTranslationPart.objects.filter(username=username, project_name=project_name)
        print(parts)
        for i, part in enumerate(parts):
            part.target_text = translated_content[i]
            part.save()
    else:
        pass


def display_translation(request, username, project_name):
    form = UploadFileForm()
    source_text_lists, target_text_lists = get_translation_data(username, project_name)
    source_text_list = json.dumps(source_text_lists)
    target_text_list = json.dumps(target_text_lists)
    return {'form': form, 'username': username, 'source_text_list': source_text_list,
            'target_text_list': target_text_list}


def main_display(request, project_name):
    username = request.session.get('username')
    updateMysqldata(request, username, project_name)
    context.update(display_translation(request, username, project_name))
    return render(request, 'main_display.html', context)


def translate(request):
    if request.method == 'POST':
        word = request.POST.get('word')
        response = connect(word)
        data = json.loads(response)
        translation = data['translation'][0]
        print('1')
        return JsonResponse({'result': translation})
    return JsonResponse({'error': 'Invalid request method'})


def ajax_match_strings(request):
    string_similarity = {}
    if request.method == 'POST':
        string1 = request.POST.get('string1')
        print(string1)
    #     source_data = TextTranslationPart.objects.values_list('source_text', flat=True)
    #     for value in source_data:
    #         string2 = value
    #         similarity_score = fuzz.ratio(string1, string2)
    #         string_similarity = {
    #             'string': string2,
    #             'similarity_score': similarity_score
    #         }
    #     string_similarity_list = list(string_similarity)
    #     # 对列表进行排序,根据 'similarity_score' 字段从大到小排序
    #     string_similarity_list.sort(key=lambda x: x['similarity_score'], reverse=True)
    #     # 取出前五个键值对
    #     top_5_strings = string_similarity[:5]
    #     return JsonResponse({'top_5_strings': top_5_strings})
    # return JsonResponse({'error': 'Invalid request'})
