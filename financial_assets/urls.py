from django.urls import path

from . import views

urlpatterns = [
    path("assets/<str:wallets_id>/", views.ListCreateAssetView.as_view()),
    path("assets/<str:wallets_id>/", views.RetrieveUpdateAssetView.as_view()),
]
