from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def hello(request):
    return HttpResponse("双击 666")

def hehe(request):
    return HttpResponse("你真是一个小天才，这就会了")


def haha(request):
    return HttpResponse("<h>睡觉的站起来</h>")


def index(request):
    return render(request,"index.html")

def home(request):
    return render(request,"home.html")