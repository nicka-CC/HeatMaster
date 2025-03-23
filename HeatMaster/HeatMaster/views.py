from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from .forms import CalculatePriceForm, CustomUserCreationForm, CustomAuthenticationForm
from .models import Thermostats


def home(request):
    thermostats = Thermostats.objects.all()
    return render(request, 'pages/home.html', {'thermostats': thermostats})

def about(request):
    return render(request, 'pages/about.html')
def calculate_price(request):
    if request.method == "POST":
        form = CalculatePriceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('calculate_price')
    else:
        form = CalculatePriceForm()
    return render(request, 'pages/calculate_price.html',{'form':form})

def signUp(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'pages/signUp.html', {'form': form})

def signIn(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'pages/signIn.html', {'form': form})