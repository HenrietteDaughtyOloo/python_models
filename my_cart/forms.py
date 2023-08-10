from django import forms
from .models import MyCart

class ProductCartForm(forms.ModelForm):
    class Meta:
        model = MyCart
        fields = "__all__"
        