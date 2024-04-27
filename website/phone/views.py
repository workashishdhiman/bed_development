from django.shortcuts import render

# Create your views here.

def phone_home(request):
    return render(request,"app/home1.html")