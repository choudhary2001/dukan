
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect

from .cart import Cart
from .forms import CheckoutForm
from main.utilities import checkout
def cart_detail(request):
    cart = Cart(request)


    if request.method == 'POST':
        form = CheckoutForm(request.POST)

        if form.is_valid():
 

            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone_no = form.cleaned_data['phone_no']
            address = form.cleaned_data['address']
            state = form.cleaned_data['state']
            district = form.cleaned_data['district']
            block = form.cleaned_data['block']
            post_office = form.cleaned_data['post_office']
            pincode = form.cleaned_data['pincode']
            landmark = form.cleaned_data['landmark']
            user = request.user

            order = checkout(request, first_name, last_name, email, phone_no, address,state,district, block, post_office, pincode , landmark,  cart.get_total_cost())

            cart.clear()


            return redirect('success')
            
            
    else:
        form = CheckoutForm()

    remove_from_cart = request.GET.get('remove_from_cart', '')
    change_quantity = request.GET.get('change_quantity', '')
    quantity = request.GET.get('quantity', 0)

    if remove_from_cart:
        cart.remove(remove_from_cart)

        return redirect('cart')
    
    if change_quantity:
        cart.add(change_quantity, quantity, True)

        return redirect('cart')

    return render(request, 'cart/cart.html',{'cart': cart, 'form':form} )


def success(request):
    return render(request, 'cart/success.html')