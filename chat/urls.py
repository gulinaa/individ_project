
from django.urls import path
from . import views

urlpatterns = [
    path('messages/<int:sender>/<int:receiver>/', views.message_list),
    path('messages/', views.message_list),
    path('users/', views.user_list),
]