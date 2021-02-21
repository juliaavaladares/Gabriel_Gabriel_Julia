from django.urls import path
from django.conf.urls import url
from.import views

app_name = 'courses'
urlpatterns = [
    path('login', views.user_login, name='login'),
    path('profile', views.profile, name='profile'),
    path('turing', views.turing, name='turing'),
    path('admin/home', views.admin_home, name='admin_home')
]