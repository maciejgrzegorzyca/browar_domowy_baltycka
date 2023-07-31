from django.urls import path
from . import views

urlpatterns = [
    path('batches/', views.batches, name='batches'),
    path('batches/details/<int:id>', views.details, name='details'),
]