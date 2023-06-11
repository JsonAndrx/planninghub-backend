from django.urls import path
from apps.users.views import users 


urlpatterns = [
    path('api/users', users.LoginUser.as_view()),
    path('api/singup', users.SingupUser.as_view())
]