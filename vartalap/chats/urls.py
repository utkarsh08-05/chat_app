from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_list, name='user_list'),

    # API endpoints
    path('messages/<int:user_id>/', views.fetch_messages, name='fetch_message'),
    path('status/<int:user_id>/', views.user_status, name='user_status'),

    # Chat page
    path('<int:user_id>/', views.chat_detail, name='chat_detail'),
]
