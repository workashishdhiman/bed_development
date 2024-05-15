from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .forms import LoginForm


urlpatterns = [
    path("", views.home, name='home'),
    path("about-us", views.aboutus, name='aboutus'),
    path("contact-us", views.contactus, name='contactus'),
    path("category/<slug:val>", views.CategoryView.as_view(),name="category"),
    path("productdetails/<int:pk>",views.ProductDetails.as_view(),name="productdetails"),
    
    #for authenticaiton
    path("CustomerRegistration",views.CustomerRegistrationView.as_view(),name="CustomerRegistration"),
    path("login",auth_view.LoginView.as_view(template_name='app/login.html',authentication_form=LoginForm),name="loginform"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)