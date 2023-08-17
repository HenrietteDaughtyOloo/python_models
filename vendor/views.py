from django.shortcuts import render
from .forms import VendorUploadForm
from .models import Vendor
from django.shortcuts import render, redirect

# Create your views here.
def vendor_upload_view(request):
    if request.method =="POST":
        form = VendorUploadForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = VendorUploadForm()
    return render(request, "vendor/vendor_upload.html", {"form": form})
def vendor_list_view(request):
    vendor = Vendor.objects.all()
    return render(request, "vendor/vendor_list.html",{"vendor":vendor})
def vendor_detail_view(request, id):
    vendor = Vendor.objects.get(id=id)
    return render(request, "vendor/vendor_detail.html", {"vendor":vendor})
def vendor_update_view(request, id):
    vendor = Vendor.objects.get(id=id)
    if request.method=="POST":
        form=VendorUploadForm(request.POST, instance=vendor)
        if form.is_valid():
            form.save()
            return redirect("vendor_detail",id=vendor.id)
    else:
        form=VendorUploadForm(instance=vendor)
    return render(request, "vendor/edit_product.html",{"form": form})
def delete_vendor(request, id):
    vendor = Vendor.objects.get(id=id)
    vendor.delete()
    return redirect("vendor_list_view")