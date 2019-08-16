from django.urls import path
from . import views

urlpatterns = [
    ## This contains path of all the urls related to consignment
    path('', views.Index, name='index-page'),
    path('about/', views.About, name='about-page'),
    path('Dashboard/', views.Dashboard, name='dashboard'),
    path('Register/', views.Register, name = 'consignment-register'),
    path('Update/', views.UpdateTrackInfo, name='consignment-update'),
    path('Track/', views.ConsignmentTrack, name='consignment-track')
]