from django.urls import path

from . import views

urlpatterns = [
    path("transactions/<str:assets_name>/", views.ListCreateTransactionView.as_view()),
    # path("assets/<str:assets_id>/", views.RetrieveUpdateAssetView.as_view()),
]
