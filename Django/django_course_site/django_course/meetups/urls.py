
from django.urls import path
from . import views
urlpatterns = [
    path('meetups', views.index),  # domain.com/meetups
    path('meetups/<meetup_slug>', views.meetup_details)
]
