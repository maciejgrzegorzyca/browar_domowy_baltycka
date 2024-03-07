from django.urls import path
from .views import (
   BlogHome, 
   BlogDetail
)



urlpatterns = [
   #Class Based View urls
   path('', BlogHome.as_view(), name='blog_home'),
   path('<int:pk>/', BlogDetail.as_view(), name='blog_detail'),

   
    # function view urls
    # path('', views.blog_home, name='blog_home'),
    # path('details/<int:id>', views.blog_detail, name='blog_detail'),

]