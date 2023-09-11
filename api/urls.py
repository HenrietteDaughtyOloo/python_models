from django.urls import path
from .views import CustomerListViews
from .views import CustomerDetailView

urlpatterns=[
    path('customers/', CustomerListViews.as_view(), name='customer_list_view'),
    path('customers/<int:pk>/', CustomerDetailView.as_view(), name='customer_retrieve_update_destroy'),
]