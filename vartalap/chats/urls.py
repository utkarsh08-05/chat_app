from django.urls import path
from . import views

urlpatterns = [
    path("", views.chat_home, name="chat_home"),
    path("<int:user_id>/", views.chat_home, name="chat_home"),

    # APIs
    path("messages/<int:user_id>/", views.fetch_messages, name="fetch_message"),
    path("status/<int:user_id>/", views.user_status, name="user_status"),
    path("active/", views.chat_active, name="chat_active"),
    path("inactive/", views.chat_inactive, name="chat_inactive"),

]
