from django.urls import path
from .views import SchedulingListCreateView, SchedulingDetailView

urlpatterns = [
    path("", SchedulingListCreateView.as_view()),
    path("<int:pk>/", SchedulingDetailView.as_view()),
]
