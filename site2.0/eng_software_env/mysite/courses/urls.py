from django.urls import path
from django.conf.urls import url
from.import views

app_name = 'courses'
urlpatterns = [
    url('login', views.user_login, name='login'),
    url('profile', views.profile, name='profile'),
]
