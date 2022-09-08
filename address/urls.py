from django.urls import path

from . import views

urlpatterns = [
    path("address/", views.AddressView.as_view()),
    path("address/<str:user_id>/", views.DetailAddressView.as_view()),
]
