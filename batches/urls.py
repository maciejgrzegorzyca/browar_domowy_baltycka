from django.urls import path
from . import views

from .views import (
   BatchesHome, 
   BatchesDetail

)

urlpatterns = [
    #Class Based View urls
   path('', BatchesHome.as_view(), name='batches_home'),
   path('<int:pk>/', BatchesDetail.as_view(), name='batches_detail'),



       
   #function view urls
   # path('', views.batches_home, name='batches_home'),
   # path('details/<int:id>', views.batches_detail, name='batches_detail'),

   
   ]

