from django.contrib import admin
from .models import UserDetail, ProductReview



class UserDetailAdmin(admin.ModelAdmin):
	list_display=(            
            'user',
			'first_name',
			'last_name',
			'email',
			'photo',
			'dob',
			'mobile',
			'alternate_mobile',
			'address',
			'pincode',
			'landmark',
			'locality',
			'city',
			'state',
			'Gender',)
admin.site.register(UserDetail,UserDetailAdmin)

class ProductReviewAdmin(admin.ModelAdmin):
	list_display=('user','product','review_text','get_review_rating')
admin.site.register(ProductReview,ProductReviewAdmin)

