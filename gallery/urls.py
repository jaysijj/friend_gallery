from django.urls import path
from .views import PhotoListCreateView, PhotoDetailView, CommentCreateView

urlpatterns = [
    path('photos/', PhotoListCreateView.as_view()),
    path('photos/<int:pk>/', PhotoDetailView.as_view()),
    path('photos/<int:pk>/comments/', CommentCreateView.as_view()),
]
