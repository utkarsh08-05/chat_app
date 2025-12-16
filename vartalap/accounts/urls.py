from django.urls import path
from .views import register, logout_view, CustomLoginView,update_profile

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path("profile/", update_profile, name="update_profile"),

]
