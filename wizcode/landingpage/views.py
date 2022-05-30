from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def TemplateView(request):
    return render(request, 'base.html')

def index(request):
    return render(request, 'index.html')

def register(request):
    username = request.POST['username']
    firstName = request.POST['firstName']
    lastName = request.POST['lastName']
    email = request.POST['email']
    gitHub = request.POST['gitHub']
    password = request.POST['password']
    confirmPwd = request.POST[confirmPwd]
    
    return render(request, 'registration.html')
