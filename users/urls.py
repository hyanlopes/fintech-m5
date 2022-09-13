from django.urls import path

from . import views

urlpatterns = [
    path("users/register/", views.UserView.as_view()),
    path("login/", views.CustomAuthToken.as_view()),
    path("users/", views.UserListView.as_view()),
    path("users/<str:user_id>/", views.UserDetailView.as_view()),
]
