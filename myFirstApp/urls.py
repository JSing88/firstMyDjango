from django.urls import path
from myFirstApp import views

# http://127.0.0.1/         홈으로 접속 
# http://127.0.0.1/app     

# http://127.0.0.1/create 
# http://127.0.0.1/read/1 
# http://127.0.0.1/delete 

urlpatterns = [
    path('', views.index), 
    path('create/', views.create),
    path('read/<pageNo>/', views.read), 
    path('delete/', views.delete),    
]