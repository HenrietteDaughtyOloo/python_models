from django.urls import path
from .views import product_upload_view
from.import views

urlpatterns= [
    path("products/get/", product_upload_view,
       name="product_get_view"),
# ....................
    path('my_cart/add/', views.add_to_cart, name='add_to_cart'),
    path('my_cart/edit/<int:cart_item_id>/', views.edit_cart_item, name='edit_cart_item'),
    path('my_cart/', views.cart_list, name='cart_list'),
]





