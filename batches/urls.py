from django.urls import path
from . import views

urlpatterns = [
    path('batches/', views.batches, name='batches')
]