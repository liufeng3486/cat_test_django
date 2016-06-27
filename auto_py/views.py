#coding=utf-8
from django.shortcuts import render,render_to_response
from django import forms
from django.http import HttpResponse
from auto_py.models import User
import os,os.path,hashlib
rootdir = ".\upload"
# Create your views here.
class UserForm(forms.Form):
    username = forms.CharField()
    headImg = forms.FileField()

def register(request):
    for a,b,c in os.walk(rootdir):
        pass
    
    if request.method == "POST":
        uf = UserForm(request.POST,request.FILES)
        if uf.is_valid():
            #获取表单信息
            username = uf.cleaned_data['username']
            headImg = uf.cleaned_data['headImg']
            #写入数据库
            user = User()
            user.username = username
            user.headImg = headImg
            print "_________________-"
            print username,headImg
            print "_________________"
            user.save()
            #return HttpResponse('upload ok!')
            for a,b,c in os.walk(rootdir):
                pass
            return render_to_response('auto_py/register.html',{'uf':uf,'c':c})
    else:
        uf = UserForm()
    return render_to_response('auto_py/register.html',{'uf':uf,'c':c})


def md5(request):
    import os
    xpath = os.getcwd()+'\upload'
    file_src = request.GET['a']
    xpath = xpath+ "\\"+file_src
    d = file(xpath,'r')
    d = d.readlines()
    return HttpResponse(d)








