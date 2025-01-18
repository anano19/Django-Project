from django.contrib import admin
from django.urls import path
from .views import index, MenuItemView, SingleMenuItemView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("", index, name='index'),
    path('menu-items/', MenuItemView.as_view(), name='menu-list'),
    path('menu-items/<int:pk>/', SingleMenuItemView.as_view(), name='single-menu-item'),
    path('api-token-auth/', obtain_auth_token),
]