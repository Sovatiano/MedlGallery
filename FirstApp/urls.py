from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.welcome, name='home'),
    path('personalwelcome/', views.mywelcome, name='personalhome'),
    path('loginpage/', views.loginpage, name='login'),
    path('logout/', views.logout_user, name='logout'),
]