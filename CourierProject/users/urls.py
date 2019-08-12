from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.Register, name='register'),
    path('redirect/', views.Login_success, name='redirect')
]