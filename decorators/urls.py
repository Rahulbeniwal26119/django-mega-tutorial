from django.urls import path
from .views import print_query, get_result

urlpatterns = [
    path("loan/<int:pk>", print_query, name="Print Query"),
    path("result/", get_result, name="get_result"),
]