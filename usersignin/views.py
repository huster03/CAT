#coding=utf-8
from django.shortcuts import render , redirect
from django.http import HttpResponse
from django import forms
from .models import User
from memorydata.models import MemoryBankDetail , MemoryBankList
from specialdata.models import TermBankList , TermBankItem
import os
from mainwds import translate
from .models import TextTranslationPart
from CAT import settings
import datetime
# Create your views here.
class UploadFileForm(forms.Form):
    file = forms.FileField()

def get_project_infos_for_user(username):
    return TextTranslationPart.objects.filter(username=username) \
                          .values('project_name', 'created_at') \
                          .distinct()
def regist(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = User.objects.create(username=username,password=password)
        termbanklist = TermBankList.objects.create(user = user)
        memorybanklist = MemoryBankList.objects.create(user = user)
        MemoryBankDetail.objects.create(user = user , memory_bank = memorybanklist)
        TermBankItem.objects.create(user = user , term_bank = termbanklist)
        user.save()
        return redirect('/login')
    return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        flag = User.objects.filter(username__exact=username,password__exact=password)
        if flag:
            request.session['username'] = username
            return redirect('/user_centre')
        else:
            return HttpResponse('用户名或密码错误,请重新登录')
    return render(request,'login.html')
def user_centre(request):
    username = request.session.get('username')

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            file_path = uploaded_file.name
            path = os.path.join(settings.MEDIA_ROOT, file_path)
            with open(path, 'wb') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)
            source, target = translate.trans(path)
            for i in range(len(source)):
                TextTranslationPart.objects.create(
                    username=username,
                    part_index=i,
                    source_text=source[i],
                    target_text=target[i],
                    project_name = uploaded_file.name,
                    create_at = datetime.datetime.now()
                )
            return redirect('/main_display/')
    else:
        form = UploadFileForm()

    project_infos = get_project_infos_for_user(username)

    return render(request, 'user_centre.html', {
        'form': form,
        'project_infos': project_infos,
        'username' : username,
    })