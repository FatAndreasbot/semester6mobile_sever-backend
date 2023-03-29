from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from common import views

urlpatterns = [
    path('profiles/', views.ProfileList.as_view()),
    path('profiles/<int:pk>/', views.ProfileDetails.as_view()),
    path('profiles/<int:pk>/room', views.RoomDetails.as_view())
]

