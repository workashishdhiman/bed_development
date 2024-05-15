from django.shortcuts import render
from django.views import View
from django.db.models import Count
from .models import Product
from .forms import CustomerRegistrationForm
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,"app/home.html")
def contactus(request):
    return render(request,"app/contactus.html")
def aboutus(request):
    return render(request,"app/aboutus.html")


class CategoryView(View):
    def get(self,request,val):
        product = Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values('title').annotate(total=Count('title'))
        return render(request,"app/category.html",locals())
    

class ProductDetails(View):
    def get(self,request,pk):
        product= Product.objects.get(pk=pk)
        return render(request,"app/product.html",locals())


class CustomerRegistrationView(View):
    def get(self,request):
        form=CustomerRegistrationForm()
        return render(request,"app/registration.html",locals())
    
    def post(self,request):
        form=CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Congratulations! user have been registered :)")
        else:
            messages.error(request,"Screen Error")
        return render(request,'app/registration.html')


