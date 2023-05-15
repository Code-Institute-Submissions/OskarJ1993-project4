from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Product, Cart
from django.http import JsonResponse


# Create your views here.

def index(request):
    phones = Product.objects.filter(category='Tires')
    chargers = Product.objects.filter(category='Rims')
    context = {'products': list(phones)}
    
    if 'message' in request.session:
        context['message'] = request.session['message']
        del request.session['message']
    
    return render(request, 'index.html', context)

def phones(request):
    products = Product.objects.filter(category='Tires')
    return render(request, 'tires.html', {'products': products})

def accessories(request):
    products = Product.objects.filter(category='Rims')
    return render(request, 'rims.html', {'products': products})
    


def search(request):
    query = request.GET.get('q')
    products = Product.objects.filter(title__icontains=query)
    context = {'products': products}
    return render(request, 'search.html', context)




def add_to_cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        quantity = request.POST.get('quantity')
        product = get_object_or_404(Product, id=product_id)
        cart = Cart.add_to_cart(request.user, product, quantity)
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error'})

def show_cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum([item.quantity * item.product.price for item in cart_items])
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})


def clear_cart(request):
    Cart.objects.filter(user=request.user).delete()
    return redirect(show_cart)

