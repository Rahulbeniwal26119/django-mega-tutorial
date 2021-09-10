from django.urls import path
from .views import StudentView

urlpatterns = [
    path("forms/", StudentView.as_view())
    ]