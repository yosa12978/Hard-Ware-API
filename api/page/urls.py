from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("", views.Index.as_view()),
    path("create/", views.Create.as_view()),
    path("signup/", views.SignUp.as_view()),
    path("token/", obtain_auth_token),
]