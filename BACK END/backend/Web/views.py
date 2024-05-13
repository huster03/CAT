from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def user_register(request):
    return render(request,'user_register.html')

def translate(request):
    if request.method == 'POST':
        return render(request, 'translate.html')
    original_language_text = request.POST.get('original_language_text')
    translated_language_text = request.POST.get('translated_language_text')
    return render(request, 'translate.html', {'original_language_text':original_language_text, 'translated_language_text':translated_language_text})

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
