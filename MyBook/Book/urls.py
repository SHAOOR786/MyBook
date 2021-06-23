from django.urls import path
from . import views

app_name = 'Book'
urlpatterns=[
    path('', views.Login,name='LogIn'),
    path('Auth/', views.Auth,  name='Auth'),
    path('SignUpPage/', views.SignUpPage,  name='SignUpPage'),
    path('SignUp/', views.SignUp,  name='SignUp')
]