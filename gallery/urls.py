from django.urls import path
from .views import PhotoListCreateView, PhotoDetailView

urlpatterns = [
    path('photos/', PhotoListCreateView.as_view()),
    path('photos/<int:pk>/', PhotoDetailView.as_view()),
]
