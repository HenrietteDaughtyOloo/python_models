from django.urls import path
from .views import customer_upload_view
from .views import customer_list
from .views import customer_detail
from .views import customer_update_view
from .views import delete_customer


urlpatterns = [
    path("products/upload/", customer_upload_view,name = "customer-upload_view"), 
    path("customers/list",customer_list,name="customer_list_view"),
    path("customers/<int:id>",customer_detail,name="customer_detail_view"),
    path("customers/edit/<int:id>",customer_update_view,name="customer_update"),
    path("customers/delete/<int:id>",delete_customer,name="customer_delete"),
]