from django.shortcuts import render,redirect
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)
def process(request):
    quantity_from_form = int(request.POST["quantity"])
    id_from_form = int(request.POST["product_id"])
    this_product = Product.objects.get(id=id_from_form)
    price = this_product.price
    total_charge = quantity_from_form * price
    print("Charging credit card...")
    Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
    return redirect('/checkout')

def checkout(request):
    last_order = Order.objects.last()
    total_charge = last_order.total_price
    total_quantity = 0
    total_spend = 0
    all_order = Order.objects.all()
    for order in all_order:
        total_quantity += order.quantity_ordered
        total_spend += order.total_price
     
    context={
        "total_charge": total_charge,
        "total_quantity": total_quantity,
        "total_spend": total_spend,
    }
    return render(request, "store/checkout.html",context)

