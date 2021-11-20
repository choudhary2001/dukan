from django.shortcuts import render
from cart.models import OrderItem
from .forms import AddToCartForm, SignupForm
from .models import UserDetail, ProductReview
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils import timezone
from product.models import Category, Banner, Product
from django.template.loader import render_to_string
from django.http import JsonResponse, HttpResponse, request,HttpResponseRedirect, response
from django.urls import reverse
from django.db.models.query_utils import Q
from django.contrib.auth.decorators import login_required
from django.db.models import Max, Min, Count, Avg
from .forms import ReviewAdd
from cart.cart import Cart


def home(request):
    cat = Category.objects.all()
    bann = Banner.objects.all()
    product = Product.objects.all().order_by('-id')
    context = {
        'cat' : cat,
        'bann' : bann,
        'product' : product,
    }
    return render(request, 'main/index.html', context)

# Signup Form
def Signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            pwd = form.cleaned_data.get('password1')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            user = User.objects.filter(username=username).first()
            if username.isdigit():
                UserDetail(user=user, mobile=username, first_name=first_name, last_name=last_name, email=email).save()
            else:
                user.email = email
                user.save()
                UserDetail(user=user, first_name=first_name, last_name=last_name, email=email).save()
                messages.success(request, f'Account is Created for {username}')
            
            return redirect('login')
    else:
        form = SignupForm
    return render(request, 'main/registration/signup.html', {'form': form})


def category_product_list(request, cat_id):
    category = Category.objects.get(id=cat_id)
    data = Product.objects.filter(category=category).order_by('-price')

    return render(request, 'main/category_product_list.html', {
        'data': data,

    })

# Filter Data

    
def search(request):
    q = request.GET['q']
    data = Product.objects.filter(Q(title__icontains=q) | Q(
        details__icontains=q)).order_by('-id')

    return render(request, 'main/search.html', {'data': data})



# Product Detail
def product_detail(request, slug, id):
    product = Product.objects.get(id=id)

    if request.user.is_authenticated:
        cart = Cart(request)
        related_products = Product.objects.filter(
        category=product.category).exclude(id=id)[:4]

        if request.method == 'POST':
            form = AddToCartForm(request.POST)
            if form.is_valid():
                quantity = form.cleaned_data['quantity']
                cart.add(product_id=product.id, quantity=quantity, update_quantity=False)
                messages.success(request, 'The product was added to the cart')
                return HttpResponseRedirect(reverse('product_detail', args=[slug,id]))

        else:
            form = AddToCartForm()


    # End

    # Fetch reviews
        reviews = ProductReview.objects.filter(product=product)
    # End

    # Fetch avg rating for reviews
        avg_reviews = ProductReview.objects.filter(
        product=product).aggregate(avg_rating=Avg('review_rating'))
    # End
        product = Product.objects.get(pk=id)
        user = request.user
        if request.method == 'POST':
            form = ReviewAdd(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.user = user
                review.product = product
                review.save()
                return HttpResponseRedirect(reverse('product_detail', args=[slug,id]))

        else:
            form = ReviewAdd()
    # End
    else:
        product = Product.objects.get(id=id)

        related_products = Product.objects.filter(
        category=product.category).exclude(id=id)[:4]

    # End

    # Fetch reviews
        reviews = ProductReview.objects.filter(product=product)
    # End

    # Fetch avg rating for reviews
        avg_reviews = ProductReview.objects.filter(
        product=product).aggregate(avg_rating=Avg('review_rating'))
    # End


    return render(request, 'main/product_detail.html', {'data': product, 'form':form, 'related': related_products,'reviews': reviews, 'avg_reviews': avg_reviews})


@login_required
def profile(request):
 

    customer = request.user

    reviews = ProductReview.objects.filter(user=request.user).order_by('-id')
    orders = OrderItem.objects.filter(user= request.user).order_by('-id')

    
    return render(request, 'main/user/profile.html', {'customer': customer, 'reviews': reviews, 'orders':orders})
