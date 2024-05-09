from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def user_add(request):
    return render(request, 'user_add.html')

def user_list(request):
    return render(request, 'user_list.html')

def user_project(request):
    return render(request, 'user_project.html')

def user_project_list(request):
    return render(request, 'user_project_list.html')

def user_memory_bank(request):
    return render(request, 'user_memory_bank.html')

def user_memory_bank_list(request):
    return render(request, 'user_memory_bank_list.html')

def user_term_bank(request):
    return render(request, 'user_term_bank.html')

def user_term_bank_list(request):
    return render(request, 'user_term_bank_list.html')
