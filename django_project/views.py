from django.http import HttpResponse
from django.shortcuts import render
def vic(request):
    return HttpResponse("hello ")
def home(request):
    return render(request,'home.html' )
def submit(request):
    data =request.GET['gender']

    return render(request,'final.html', {'data1':data} )