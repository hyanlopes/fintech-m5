from django.urls import path

from . import views

urlpatterns = [
    path("users/register/", views.UserView.as_view()),
]
