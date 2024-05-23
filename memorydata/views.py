from django.shortcuts import render

# Create your views here.
def user_certre(request):
    return render(request, 'user_centre.html')
def memo_bank(request):
    return render(request, 'memo_bank.html')