from django.shortcuts import get_object_or_404, redirect, render

from .forms import OrderForm
from .models import Order


def home_view(request):
    context = {
        "orders_count": Order.objects.count(),
    }
    return render(request, "index.html", context)


def order_create_view(request):
    form = OrderForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("order_list")

    return render(request, "crudapp/order.html", {"form": form, "page_title": "Create Order"})


def order_list_view(request):
    orders = Order.objects.all()
    return render(request, "crudapp/show.html", {"orders": orders})


def order_update_view(request, pk):
    order = get_object_or_404(Order, pk=pk)
    form = OrderForm(request.POST or None, instance=order)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("order_list")

    return render(request, "crudapp/order.html", {"form": form, "page_title": "Update Order"})


def order_delete_view(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == "POST":
        order.delete()
        return redirect("order_list")

    return render(request, "crudapp/confirmation.html", {"order": order})
