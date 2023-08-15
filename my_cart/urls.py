from django.urls import path
from .views import product_upload_view
from .views import cart_list
from .views import add_to_cart
from .views import edit_cart_item
from.import views

urlpatterns= [
    path("products/get/", product_upload_view,
    name="product_get_view"),
# ....................
    path('my_cart/add/', add_to_cart, name='add_to_cart'),
    path('my_cart/edit/<int:id>/', edit_cart_item, name='edit_cart_item'),
    path('my_cart/list', cart_list, name='cart_list'),

]




