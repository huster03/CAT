"""
URL configuration for Backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from Web import views

urlpatterns = [
    path('home/',views.home),
    path('login/',views.login),
    path('uesr/add/',views.user_add),
    path('user/project/list/',views.user_project_list),
    path('user/project/',views.user_project),
    path('user/memory bank/list/',views.user_memory_bank_list),
    path('user/memory bank/',views.user_memory_bank),
    path('user/term bank/list/',views.user_term_bank_list),
    path('user/term bank/',views.user_term_bank),
]
