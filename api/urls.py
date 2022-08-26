from django.urls import path
from .views import CustomerList
from .views import CustomerDetail

urlpatterns = [
    path("customers/", CustomerList.as_view()),
    path("customer/<int:pk>/", CustomerDetail.as_view()),
]
