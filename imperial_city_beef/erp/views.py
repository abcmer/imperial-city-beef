from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse


from .models import Product, Cart

def index(request):
    return render(request, 'erp/index.html')
    # return HttpResponse("Welcome to Imperial City Beef")

def products(request):
    products = Product.objects.all()    
    context = {'products': products}
    return render(request, 'erp/products.html', context)

def product_detail(request, product_id):
    try:
        product = get_object_or_404(Product, id=product_id)
        context = {'product': product}
        return render(request, 'erp/product_detail.html', context)
    except Product.DoesNotExist:
        raise Http404('Product does not exist')

def cart(request):
    cart_items = Cart.objects.filter(customer_id='9e4cdba9-17db-4c8e-87d0-df28ad428c79').select_related('product')    
    context = {'cart_items': cart_items}
    return render(request, 'erp/cart.html', context)        


    