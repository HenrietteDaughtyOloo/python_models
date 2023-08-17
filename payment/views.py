from django.shortcuts import render

from .forms  import PaymentUploadForm
from .models import Payment
# Create your views here.

def payment_create_view(request):
    if request.method == "POST":
        form = PaymentUploadForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect("payment_success")  # Redirect to a success page
    else:
        form = PaymentUploadForm()

    return render(request, 'payment_form.html', {'form': form})
