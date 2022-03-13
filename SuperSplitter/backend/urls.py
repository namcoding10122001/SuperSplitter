from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerUser, name='register'),
    path('profiles/', views.profiles, name='profiles'),
    path('profiles/<str:pk>', views.user_profile, name='user-profile')

]