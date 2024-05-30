# coding=utf-8
import PyPDF2
from django import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect
# Create your views here.
from docx import Document

from mainwds.translation import connect
from mainwds import translate
from mainwds.views import get_translation_data
from memorydata.models import Memorydatatable
from specialdata.models import Specialdatatable
from .models import TextTranslationPart
from .models import User


class UserForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=50)
    password = forms.CharField(label='密码', widget=forms.PasswordInput())
    email = forms.EmailField(label='邮箱')


class UploadFileForm(forms.Form):
    file = forms.FileField()


def regist(request):
    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            username = userform.cleaned_data['username']
            password = userform.cleaned_data['password']
            email = userform.cleaned_data['email']
            user = User.objects.create(username=username, password=password, email=email)
            Memorydatatable.objects.create(user=user)
            Specialdatatable.objects.create(user=user)
            user.save()
        return HttpResponse('regist success!!!')
    else:
        userform = UserForm()
    return render(request, 'regist.html', {'userform': userform})


def login(request):
    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            username = userform.cleaned_data['username']
            password = userform.cleaned_data['password']

            flag = User.objects.filter(username__exact=username, password__exact=password)

            if flag:
                request.session['username'] = username
                if get_translation_data(username) != (None, None):
                    print(get_translation_data(username))
                    return redirect('/main_display')
                else:
                    return redirect('/uploadFile')
            else:
                return HttpResponse('用户名或密码错误,请重新登录')

    else:
        userform = UserForm()
    return render(request, 'login.html', {'userform': userform})


def upload_file(request):
    form = UploadFileForm()
    if request.method == 'POST':
        username = request.session.get('username')
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            with open('media/copy_file.txt', 'wb+') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)

            file_extension = uploaded_file.name.split('.')[-1]

            # 根据文件扩展名进行不同的处理
            if file_extension == 'txt':
                # 打开保存的txt文件，并读取内容
                with open('media/copy_file.txt', 'r', encoding='utf-8') as file:
                    lines = file.readlines()

            elif file_extension == 'docx':
                # 使用python-docx库读取docx文件内容
                doc = Document('media/copy_file.txt')
                lines = [paragraph.text for paragraph in doc.paragraphs]

            elif file_extension == 'pdf':
                # 使用PyPDF2库读取PDF文件内容
                with open('media/copy_file.txt', 'rb') as file:
                    pdf_reader = PyPDF2.PdfReader(file)
                    lines = []
                    for page in pdf_reader.pages:
                        lines.append(page.extract_text())
            with open('media/last_copy.txt', 'w', encoding='utf-8') as file:
                file.writelines(lines)
            path = 'media/last_copy.txt'
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
    return render(request, 'uploadFile.html', {'form': form})
