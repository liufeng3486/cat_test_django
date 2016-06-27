from django.shortcuts import render
from django.http import HttpResponse
import hashlib
# Create your views here.

def index(request):
    return render(request, 'md5_encoding\index.html')
    
def md5(request):
    data = request.GET['a']
    m = hashlib.md5()   
    m.update(data)
    return HttpResponse(m.hexdigest())

