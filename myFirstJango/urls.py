"""myFirstJango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# http://127.0.0.1/         홈으로 접속 
# http://127.0.0.1/app     

# http://127.0.0.1/create 
# http://127.0.0.1/read/1 

urlpatterns = [
    # 'admin/' 장고가 가지고 있는 기본적인 관리자 화면으로 이동하는 url
    path('admin/', admin.site.urls),
    # 클라이언트가 접속을 시도하였을 시, admin이 아닌 다른 주소로 접속을 
    # 시도하게 될 경우 "myFirstApp" 의 urls.py로 위임을 하게 되는 것 
    path('', include('myFirstApp.urls')),

    # path('app/', include('myFirstApp.urls'))   app에 접속

]
