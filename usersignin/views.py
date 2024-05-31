# coding=utf-8
import datetime
import PyPDF2
import datetime
from django import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect
from docx import Document
from memorydata.models import MemoryBankDetail
from specialdata.models import TermBankList
from mainwds import translate
from .models import TextTranslationPart
from .models import User


class UserForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=50)
    password = forms.CharField(label='密码', widget=forms.PasswordInput())
    email = forms.EmailField(label='邮箱')

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
        MemoryBankDetail.objects.create(user = user)
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
            return redirect('/user_centre')
        else:
            return HttpResponse('用户名或密码错误,请重新登录')
    return render(request,'login.html')
def user_centre(request):
    username = request.session.get('username')
    form = UploadFileForm()

    if request.method == 'POST':
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
                    project_name = uploaded_file.name,
                    source_text=source[i],
                    target_text=target[i],
                    create_at = datetime.datetime.now()
                )
            return redirect('/main_display/')

    project_infos = get_project_infos_for_user(username)

    return render(request, 'user_centre.html', {
        'form': form,
        'project_infos': project_infos,
        'username' : username,
    })