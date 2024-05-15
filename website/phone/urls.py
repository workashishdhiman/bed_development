from django.urls import path
from . import views

urlpatterns = [
    path("",views.phone_home,name="phone_home"),
    path("aboutus",views.phone_aboutus,name="phone_aboutus"),
    path("contactus",views.phone_contactus,name="phone_contactus"),
    path("CategoryPhone/<slug:valu>/",views.CategoryViewPhone.as_view(),name="categoryPhone"),
    path("ProductPhone/<slug:pk>/",views.ProductViewPhone.as_view(),name="ProductPhone"),
]
