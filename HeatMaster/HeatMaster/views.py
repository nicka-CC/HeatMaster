from django.shortcuts import render, redirect

from .forms import CalculatePriceForm
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
        print('hh')
    return render(request, 'pages/calculate_price.html',{'form':form})