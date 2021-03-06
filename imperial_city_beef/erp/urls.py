from django.urls import path

from . import views

app_name = 'erp'
urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.products, name='products'),
    path('products/<uuid:product_id>/', views.product_detail, name='product_detail'),
    path('cart/<uuid:customer_id>', views.cart, name='cart'),
    path('cart/checkout/<uuid:customer_id>', views.checkout, name='checkout'),
    path('logout/', views.logout_view, name='logout')

]