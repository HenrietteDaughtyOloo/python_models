from django.urls import path
from .views import CustomerListViews

urlpatterns=[
    path('customers/', CustomerListViews.as_view(), name='customer_list_view'),
]