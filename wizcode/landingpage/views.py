from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .form import RegistrationForm


# Create your views here.

def TemplateView(request):
    return render(request, 'base.html')

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect("landingpage:index")
        messages.error(request, "Unsuccessful Registration. Invalid Information.")
    form = RegistrationForm()
    return render(request, 'registration.html')
    
def login(request):
    return render(request, 'login.html')















# else:
        #     firstName = request.POST['firstName']
        #     lastName = request.POST['lastName']
        #     email = request.POST['email']
        #     gitHub = request.POST['gitHub']
        #     userName = request.POST['userName']
        #     password = request.POST['password']
        #     confirmPwd = request.POST['confirmPwd']
        #     if password == confirmPwd:
        #         if User.objects.filter(email = email).exists():
        #             messages.info(request, 'Email Already Used')
        #             return redirect('register')
        #         elif User.objects.filter(userName = userName).exists():
        #             messages.info(reques, 'Username Already Used')
        #             return redirect('register')
        #         else:
        #             user = User.objects.create_user(userName = userName, email = email, password = password)
        #             user.save()
        #             return redirect('login')
        #     else:
        #         messages.info(request, 'Password not the same')
        #         return redirect('register')
        # else:
        #     messages.info(request, 'All fields are required')
    