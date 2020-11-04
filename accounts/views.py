from django.shortcuts import render, redirect

# Create your views here.
def logout(request):
    return redirect('home')

def login(request):
    return render(request, 'accounts/login.html')

def register(request):
    return render(request, 'accounts/register.html')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')