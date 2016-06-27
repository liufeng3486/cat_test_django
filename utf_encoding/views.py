from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#def index(req):
 #   return render(req,'utf_encoding\index.html')


def index(request):
    return render(request, 'utf_encoding\index.html')
    
def add(request):
    string=''
    data = request.GET['a']
    for i in range(0,len(data),2):
        string += chr((int(data[i],16)<<4)+int(data[i+1],16))
    return HttpResponse(string)



