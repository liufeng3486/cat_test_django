# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from django.shortcuts import render
from test1.models import Person,Request,Log,Request_Data
from django.http import HttpResponse
import time,random,datetime
import urllib2,urllib

# Create your views here.
# 这个方法需要独立出去
def log_insert(url_src,data_src,type_src,name_src,res_src,poll_id):
    Log(url=url_src,
        data=data_src,
        type=type_src,
        name=name_src,
        response=res_src,
        poll =poll_id ).save()
def data_manage(value):
    temp = str(value).split('!.!')
    if len(temp) > 1:
        if temp[0] == 'random':
            data = ''
            for i in range(int(temp[1])):
                if i == 0:
                    data += str(random.randint(1,9))
                else:
                    data += str(random.randint(0,9))
            return data
        elif temp[0]== 'time':
            data = ''
            if temp[1]=='now':
                data = str(datetime.datetime.now())
                print data
                return data
    return False
def index(req):
    Request_List = Request.objects.all()
    context = {'Request_List':Request_List}
    return render(req,'test1/index.html',context)
#post相关
def post_ready(req,test1_id):
    prc = Request.objects.get(id=test1_id)
    temp = Request_Data.objects.filter(f_key=test1_id)
    print prc.url
    data = {}
    for i in temp:
        data_temp = data_manage(i.value)
        if data_temp:
            data[str(i.key)]=data_temp
            print data[str(i.key)]
            print type(data[str(i.key)])
        else:
            if i.value=="null":
                data[str(i.key)]=''
            else:     
                data[str(i.key)]=str(i.value)
    context = {'url':prc.url,'data':data,'name':prc.name}
    return render(req,'test1/post_sub.html',context)
def post_ok(req,test1_id):
    data_src={}
    for i in req.GET:
        if i != 'url':
            data_src[i]=req.GET[i]
    url = req.GET['url']    
    data = urllib.urlencode(data_src)
    url2 = urllib2.Request(url,data)
    response = urllib2.urlopen(url2)
    apicontent = response.read()
    log_insert(url,data_src,'POST',
               Request.objects.get(id=test1_id).name,apicontent,
               Request.objects.get(id=test1_id))
    return HttpResponse(apicontent)
#get相关
def get_ready(req,test1_id):
    prc = Request.objects.get(id=test1_id)
    temp = Request_Data.objects.filter(f_key=test1_id)
    data = {}
    for i in temp:
        if i.value=="null":
            data[str(i.key)]=''
        else:     
            data[str(i.key)]=str(i.value)
    context = {'url':prc.url,'data':data,'name':prc.name}
    return render(req,'test1/post_sub.html',context)
def get_ok(req,test1_id):
    url_src = req.GET['url']
    url = url_src+"?"
    for i in req.GET:
        if i != 'url':
            url += i+"="+req.GET[i]+"&"
    url = url[:-1]
    data_src = url.split('?')[1]
    req = urllib2.Request(url)
    res_data = urllib2.urlopen(req)
    res = res_data.read()
    log_insert(url_src,data_src,'GET',
               Request.objects.get(id=test1_id).name,res,
               Request.objects.get(id=test1_id))
    return HttpResponse(res)

def get_title():
    person_list = Person.objects.all()
    print person_list


