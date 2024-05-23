#coding=utf-8
from django.shortcuts import render , redirect
from django.http import HttpResponse
from django import forms
from .models import User
from memorydata.models import Memorydatatable
from specialdata.models import TermBankList
import os
from mainwds import translate
from .models import TextTranslationPart
from CAT import settings
from mainwds.views import get_translation_data
# Create your views here.
class UploadFileForm(forms.Form):
    file = forms.FileField()
def regist(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = User.objects.create(username=username,password=password)
        Memorydatatable.objects.create(user = user)
        TermBankList.objects.create(user = user)
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
            if get_translation_data(username) != (None,None) :
                print(get_translation_data(username))
                return redirect('/main_display')
            else:
                return redirect('/uploadFile')
        else:
            return HttpResponse('用户名或密码错误,请重新登录')
    return render(request,'login.html')

def upload_file(request):
    form =  UploadFileForm()
    if request.method == 'POST':
        username = request.session.get('username')
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            file_path = uploaded_file.name
            path = os.path.join(settings.MEDIA_ROOT, file_path)
            with open(path, 'wb') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)
            source, target = translate.trans(path)

            # 按索引分段保存到数据库
            for i in range(len(source)):
                TextTranslationPart.objects.create(
                    username=username,
                    part_index=i,
                    source_text=source[i],
                    target_text=target[i]
                )
            return redirect('/main_display/')
    return render(request,'uploadFile.html',{'form':form})