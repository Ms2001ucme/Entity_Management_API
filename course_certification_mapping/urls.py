from django.urls import path
from .views import CourseCertificationMappingListCreateAPIView, CourseCertificationMappingDetailAPIView
urlpatterns = [
    path('course-certifications/', CourseCertificationMappingListCreateAPIView.as_view()),
    path('course-certifications/<int:pk>/', CourseCertificationMappingDetailAPIView.as_view()),
]