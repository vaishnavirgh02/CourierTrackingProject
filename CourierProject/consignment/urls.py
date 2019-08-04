from django.urls import path
from . import views

urlpatterns = [
    ## This contains path of all the urls related to consignment
    path('', views.Index),
    path('Dashboard/', views.Dashboard)
]