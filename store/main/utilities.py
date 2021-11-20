from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from cart.cart import Cart

from cart.models import Order, OrderItem

def checkout(request, first_name, last_name, email, phone_no, address,state , district, block, post_office, pincode, landmark,  amount):
    order = Order.objects.create(user=request.user, first_name=first_name, last_name=last_name, email=email, address=address, state=state, district=district,block = block,post_office=post_office, pincode=pincode, landmark=landmark, phone_no=phone_no, paid_amount=amount)

    for item in Cart(request):
        OrderItem.objects.create(order=order, product=item['product'], user=request.user, price=item['product'].price, quantity=item['quantity'])
    
        

    return order


