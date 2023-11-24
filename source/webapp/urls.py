from django.urls import path
from webapp.views import index, play

urlpatterns = [
    path('', index),
    path('play', play)
]
