from django.db import models
import uuid

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class InventoryMovement(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.IntegerField()

    def __str__(self):
        return f'{self.product} changed by {self.count} units.'

class Customer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    shipping_address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=12)

    def __str__(self):
        return f'{self.name}'        

class SalesOrder(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_date = models.DateTimeField()

    def __str__(self):
        return f'Sales Order: {self.id}'     

class SalesOrderDetail(models.Model):
    sales_order = models.ForeignKey(SalesOrder, on_delete=models.CASCADE)    
    product = models.ForeignKey(Product, on_delete=models.CASCADE)   
    count = models.IntegerField()

    def __str__(self):
        return f'Sales Order Detail: {self.sales_order.id}'    



