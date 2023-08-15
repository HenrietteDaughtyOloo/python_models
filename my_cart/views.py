from django.shortcuts import render
from .forms import ProductCartForm
# ...............

from django.shortcuts import render, get_object_or_404, redirect
from .models import MyCart

# from .forms import CartForm
def product_upload_view(request):
    form = ProductCartForm()
    return render(request,"cart/product_get.html",{"form": form})

# ......................
def add_to_cart(request):
    if request.method == 'POST':
        form = ProductCartForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cart_list')
    else:
        form = ProductCartForm()
    return render(request, 'cart/add_to_cart.html', {'form': form})
def edit_cart_item(request, id):
    cartlist= MyCart.objects.get(id=id)
    
    if request.method == 'POST':
        form = ProductCartForm(request.POST, instance=cartlist)
        if form.is_valid():
            form.save()
            return redirect('cart_list')
    else:
        form = ProductCartForm(instance=cartlist)
    return render(request, 'cart/edit_cart_item.html', {'form': form, 'cart_item': cartlist})
def cart_list(request):
    cart_items = MyCart.objects.all()
    return render(request, 'cart/cart_list.html', {'cart_items': cart_items})





