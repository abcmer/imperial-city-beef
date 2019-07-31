from django.contrib import admin

from .models import (
    Product,
    InventoryMovement,
    Customer,
    SalesOrder,
    SalesOrderDetail
)

admin.site.register(Product)
admin.site.register(InventoryMovement)
admin.site.register(Customer)
admin.site.register(SalesOrder)
admin.site.register(SalesOrderDetail)