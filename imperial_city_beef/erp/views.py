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

def cart(request, customer_id):
    if request.method == 'GET':
        cart_items = Cart.objects.filter(customer_id=customer_id).select_related('product') 
        context = {
            'cart_items': cart_items,
            'customer_id': customer_id
            }
        return render(request, 'erp/cart.html', context) 

    if request.method == 'POST':
        product_id = request.environ['QUERY_STRING'].split('=')[1]
        product = Product.objects.get(id=product_id)

        cart_add = Cart(customer_id=customer_id, product_id=product_id, count=1)
        cart_add.save()

        products = Product.objects.all()    
        context = {
            'products': products,
            'product_added_to_cart': product.name
            }
        return render(request, 'erp/products.html', context)


def checkout(request, customer_id):
    Cart.objects.filter(customer_id=customer_id).delete()
    context = {}
    return render(request, 'erp/checkout.html', context)   


    