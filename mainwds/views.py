from django import forms
from django.http import JsonResponse
from django.shortcuts import render
from usersignin.models import User
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





def main_display(request):
    username = request.session.get('username')
    user = User.objects.get(username=username)
    user_id = user.id
    updateMysqldata(request,username)
    context.update(display_translation(request, username))
    return render(request, 'main_display.html', context)
