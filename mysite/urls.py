"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
# -*- coding:utf-8 -*-
__author__ = "MuT6 Sch01aR"

# -*- coding:utf-8 -*-
__author__ = "MuT6 Sch01aR"

from django.conf.urls import url
from django.shortcuts import HttpResponse, render, redirect
from django.contrib import admin
from django.urls import path
from login import views
from django.urls import include


# def register(request):
#     error_msg = ""
#     if request.method == "POST":
#         username = request.POST.get("username", None)
#         password = request.POST.get("password", None)
#         print(username, password)
#         if username == username and password == password:
#             return HttpResponse('注册成功')
#         else:
#             error_msg = "注册失败"
#     return render(request, "register.html", {"error": error_msg})
#
#
# def login(request):
#     error_msg = ""
#     if request.method == "POST":
#         username = request.POST.get("username", None)
#         password = request.POST.get("password", None)
#         print(username, password)
#         if username == 'root' and password == 'root':
#             return redirect("https://www.baidu.com")
#         else:
#             error_msg = "用户名或密码错误"
#     return render(request, "login.html", {"error": error_msg})


# 保存路径和函数的对应关系

urlpatterns = [
    # url(r'^login/', login),
    # url(r'^register/', register),
    # url(r'^admin/', admin),
    # url(r'^admin/', admin.site.urls),
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('login/', views.login),
    path('register/', views.register),
    path('logout/', views.logout),
    path('captcha/', include('captcha.urls'))

]
