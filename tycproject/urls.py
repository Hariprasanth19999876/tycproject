"""
URL configuration for tycproject project.

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
from tycapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('forgot-password/', views.forgot_password_view, name='forgot_password'),
    path('rohs_list', views.rohs_list, name='rohs_list'),
    path('rohs_edit/<int:pk>/', views.rohs_edit, name='rohs_edit'),
    path('reach_list', views.reach_list, name='reach_list'),
    path('reach_edit/<int:pk>/', views.reach_edit, name='reach_edit'),
    path('add/', views.add_tycdata, name='add_tycdata'),
]
