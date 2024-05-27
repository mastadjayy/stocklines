from django.contrib.auth import views
from django.urls import path

from .forms import CustomAuthForm

app_name = 'accounts'

urlpatterns = [
    path('login/',
         views.LoginView.as_view(template_name='accounts/registration/login.html', authentication_form=CustomAuthForm),
         name='login'),
]
