"""cbv_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from django.urls import path, include
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    path('list/', views.SchoolListView.as_view(), name='school_list'),
    path('list/<slug:pk>/', views.SchoolDetailView.as_view(), name='school_detail'),
    path('create/', views.SchoolCreateView.as_view(), name='school_create'),
    path('update/<slug:pk>/', views.SchoolUpdateView.as_view(), name='school_update'),
    path('delete/<slug:pk>/', views.SchoolDeleteView.as_view(), name='school_delete'),

]
