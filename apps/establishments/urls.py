from django.urls import path
from .views import EstablishmentDetailView

urlpatterns = [
    path("", EstablishmentDetailView.as_view()),
]
