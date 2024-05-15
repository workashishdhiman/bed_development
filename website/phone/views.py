from django.shortcuts import render
from django.views import View
from . models import Devices
from django.db.models import Count

# Create your views here.

def phone_home(request):
    return render(request,"app/home1.html")
def phone_contactus(request):
    return render(request,"app/contactus1.html")
def phone_aboutus(request):
    return render(request,"app/aboutus1.html")

class CategoryViewPhone(View):
    def get(self,request,valu):
        devices = Devices.objects.filter(Category=valu)
        name = Devices.objects.filter(Category=valu).values('Name').annotate(total=Count('Name'))
        return render(request,'app/category1.html',locals())
    

class ProductViewPhone(View):
    def get(self,request,pk):
        product = Devices.objects.filter(pk=pk)
        return render(request,'app/product1.html',locals())