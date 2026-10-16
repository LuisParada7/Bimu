from django.shortcuts import render

def index(request):
    return render(request,'index/index.html',{})

def indexito(request):
    return render(request,'bryancito/indexito.html',{})
