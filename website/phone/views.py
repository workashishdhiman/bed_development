from django.shortcuts import render
from django.views import View

# Create your views here.

def phone_home(request):
    return render(request,"app/home1.html")

class CategoryViewPhone(View):
    def get(self,request,valu):
        return render(request,'app/category1.html',locals())