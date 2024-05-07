from django.urls import path
from . import views

urlpatterns = [
    path("",views.phone_home,name="phone_home"),
    path("CategoryPhone/<slug:valu>/",views.CategoryViewPhone.as_view(),name="categoryPhone"),
]
