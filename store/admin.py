from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order

# Register your models here.
class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']

class AdminCategory(admin.ModelAdmin):
    list_display = ['name']

class CustomerData(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone', 'email', 'password']

class CustomerOrders(admin.ModelAdmin):
    list_display = ['product','customer', 'quantity', 'address', 'phone', 'status']

    
admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Customer, CustomerData)
admin.site.register(Order, CustomerOrders )