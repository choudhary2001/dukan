from django.contrib import admin
from.models import OrderItem, Order

# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display=(
             'user',
			'first_name',
			'last_name',
			'email',
            'phone_no',
			'address',
			'state',
			'district',
			'block',
			'post_office',
			'pincode',
			'landmark',
			'created_at',
			'paid_amount',

    )
admin.site.register(Order, OrderAdmin)


class OrderItemAdmin(admin.ModelAdmin):
    list_display =(
        'user',
        'order',
        'product',
        'user_paid',
        'price',
        'quantity',
        
    )
admin.site.register(OrderItem,OrderItemAdmin)