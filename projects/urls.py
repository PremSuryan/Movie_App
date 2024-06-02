"""
URL configuration for projects project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from app import views
# from rest_framework.authtoken.views import obtain_auth_token
# from app.views import logout_view, CustomAuthToken

urlpatterns = [
    path('login/', views.login,name='login'),
    path('', views.login_page, name='login_page'),    # Login page
    path('register/', views.register_page, name='register'), 
    path('admin/', admin.site.urls),
    path('datainsert/',views.insert,name='insert'),
    path('displayall/',views.view,name='view'),
    path('update/<int:id>/',views.updatedata,name='update'),
    path('details/<int:id>/',views.user_comments,name='details'),
    path('commentview/<int:id>/',views.comment_view,name='comment_view'),
    # path('', views.render_login_page, name='login_page'), 
    # path('login/', obtain_auth_token,name='login'),
    # path('api-token-auth/', CustomObtainAuthToken.as_view(), name='api_token_auth'),
    # path('api-token-logout/', logout_view, name='api_token_logout'),
    # path('api-token-auth/', CustomAuthToken.as_view(), name = 'api-token-auth')
]
