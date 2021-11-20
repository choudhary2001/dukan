from product.models import Product
from django.db.models import Min,Max
def get_filter(request):
	cats=Product.objects.distinct().values('category__title','category__id')
	minMaxPrice=Product.objects.aggregate(Min('price'),Max('price'))
	
	data={
		'cats':cats,
		'minMaxPrice':minMaxPrice,
	}
	return data