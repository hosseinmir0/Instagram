from django.urls import path
from . import views

urlpatterns = [
    path("", views.FindPassword.as_view(), name="rest_password_instagram"),
    path("success/", views.Success.as_view(), name="success"),
]