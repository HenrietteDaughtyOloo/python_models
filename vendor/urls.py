from django.urls import path
from .views import vendor_upload_view
from .views import vendor_list_view
from .views import vendor_detail_view
from .views import vendor_update_view
from .views import delete_vendor

urlpatterns = [
    path("vendors/upload/", vendor_upload_view,
     name = "vendors_upload_view"),
    path("vendors/list/", vendor_list_view, 
    name="vendors_list_view"),
    path("vendors/<int:id>/", vendor_detail_view, name="product_detail_view"),
    path("vendors/edit/<int:id>/", vendor_update_view, name="product_update_view"),
    path("vendors/edit/<int:id>/",delete_vendor,
    name="vendor_update_view"),
]