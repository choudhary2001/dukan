from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls.conf import include

urlpatterns = [
    path('', views.home, name='home'),
    path('main/signup',views.Signup, name='signup'),
    path('category-product-list/<int:cat_id>',views.category_product_list,name='category-product-list'),
    path('search',views.search,name='search'),
    path('product/<str:slug>/<int:id>',views.product_detail,name='product_detail'),
    path('accounts/profile/',views.profile, name='profile'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    