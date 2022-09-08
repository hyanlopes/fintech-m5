from django.urls import path

from . import views

urlpatterns = [
    path("address/all/", views.AddressView.as_view()),
    # path("address/<str:user_id>/", ""),
]
