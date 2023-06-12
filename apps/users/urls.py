from django.urls import path
from apps.users.views import users 


urlpatterns = [
    path('api/home', users.LoginUser.as_view()),
    path('api/signup', users.SignupUser.as_view())
]