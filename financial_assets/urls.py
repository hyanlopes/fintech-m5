from django.urls import path

from . import views

urlpatterns = [
    path("assets/", views.ListCreateAssetView.as_view()),
    path("assets/<pk>/", views.RetrieveUpdateAssetView.as_view()),
]
