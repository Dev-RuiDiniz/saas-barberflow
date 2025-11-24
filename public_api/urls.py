from django.urls import path
from .views import PublicBookingView

urlpatterns = [
    path("booking/", PublicBookingView.as_view()),
]
