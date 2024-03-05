from django.urls import path
from . import views

urlpatterns = [
    path('', views.batches_home, name='batches_home'),
    path('details/<int:id>', views.batches_detail, name='batches_detail'),
]